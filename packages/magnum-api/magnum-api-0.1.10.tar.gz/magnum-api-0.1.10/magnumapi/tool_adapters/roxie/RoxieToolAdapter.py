import os
import time
import platform
from subprocess import Popen, PIPE
import xml.etree.ElementTree as ET

import pandas as pd
import numpy as np
import plotly.express as px

from magnumapi.tool_adapters.ToolAdapter import ToolAdapter
import magnumapi.tool_adapters.roxie.RoxieAPI as RoxieAPI
import magnumapi.commons.text_file as text_file

END_OF_ROXIE_CALCULATION = '     *                 END OF THIS ROXIE CALCULATION                 * '


class RoxieToolAdapter(ToolAdapter):
    """ A RoxieToolAdapter class with methods to execute a ROXIE model from command line, read figures of merit table
    and prepare a Lorentz force file

    """

    def __init__(self,
                 input_folder_rel_dir: str,
                 input_file: str,
                 output_file: str,
                 cadata_file: str,
                 xml_output_file: str) -> None:
        """ A constructor of a RoxieToolAdapter instance

        :param input_folder_rel_dir: a relative path to a directory with inputs
        :param input_file_path: a name of an input file, .data
        :param output_file_path: a name of an output file, .output
        :param cadata_file_path: a name of a cadata file, .cadata
        :param xml_output_file_path: a name of an xml output file with plots, .xml
        """
        self.input_folder_rel_dir = input_folder_rel_dir
        self.input_file_path = os.path.join(input_folder_rel_dir, input_file)
        self.output_file_path = os.path.join(input_folder_rel_dir, output_file)
        self.cadata_file_path = os.path.join(input_folder_rel_dir, cadata_file)
        self.cadata_file = cadata_file
        self.xml_output_file_path = os.path.join(input_folder_rel_dir, xml_output_file)
        self.output_lines = []

    def run(self) -> None:
        # if input.output file exists, delete it before running the model
        if os.path.isfile(self.output_file_path):
            os.remove(self.output_file_path)

        # Different execution modes depending on the operating system
        command = self._get_process_command()
        p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        byte_output, _ = p.communicate(b"input data that is passed to subprocess' stdin")

        byte_output_decode = byte_output.decode()
        self.output_lines = byte_output_decode.split('\n')

    def _get_process_command(self) -> list:
        """ Private method returning a command for a process instantiation

        """
        raise NotImplementedError('This method is not implemented for this class')

    def display_output(self) -> None:
        """ Method displaying output in case of ROXIE simulation failure

        """
        if END_OF_ROXIE_CALCULATION not in self.output_lines:
            for output_line in self.output_lines:
                print(output_line)

    @staticmethod
    def convert_figures_of_merit_to_dict(fom_df: pd.DataFrame) -> dict:
        b3 = fom_df[(fom_df.index == 'B') & (fom_df['S1'] == 3)]['OBJECTIVE.1'].values[0]
        b5 = fom_df[(fom_df.index == 'B') & (fom_df['S1'] == 5)]['OBJECTIVE.1'].values[0]
        margmi = fom_df[fom_df.index == 'MARGMI']['OBJECTIVE.1'].values[0]
        bigb = fom_df[fom_df.index == 'BIGB']['OBJECTIVE.1'].values[0]

        return {'b3': b3, 'b5': b5, 'margmi': margmi, 'bigb': bigb}

    def read_figures_of_merit_table(self) -> pd.DataFrame:
        N_OBJECTIVES_KEYWORD = 'NUMBER OF OBJECTIVES AND CONSTRAINTS'
        output_file = open(self.output_file_path, 'r')
        output_lines = output_file.read().split('\n')
        output_file.close()
        idx_start_obj_table, n_objectives = RoxieAPI.find_index_start_and_length_objective_table(output_lines,
                                                                                                 N_OBJECTIVES_KEYWORD)
        objective_table_df = RoxieAPI.extract_objective_table(output_lines, idx_start_obj_table, n_objectives)
        return objective_table_df

    @staticmethod
    def parse_roxie_xml(file_path: str) -> pd.DataFrame:
        """ Static method parsing a ROXIE XML file and returning a dataframe with strand positions and field values

        :param file_path: a path to a file
        :return: output dataframe with strand positions and field values
        """
        mytree = ET.parse(file_path)
        mytree.getroot().get('x')

        x_values = []
        y_values = []

        for type_tag in mytree.getroot().findall('loop/step/loop/step/loop/coilGeom/strands/p'):
            x_value = float(type_tag.get('x'))
            y_value = float(type_tag.get('y'))
            x_values.append(x_value)
            y_values.append(y_value)

        x_strands = []
        y_strands = []
        for i in range(0, len(x_values), 4):
            x_strands.append(np.mean(x_values[i:i + 4]))
            y_strands.append(np.mean(y_values[i:i + 4]))

        if not mytree.getroot().findall('loop/step/loop/step/loop/step/coilData'):
            raise IndexError('The XML file does not contain coilData with results. '
                             'Please enable plotting in the ROXIE file')

        data_str = mytree.getroot().findall('loop/step/loop/step/loop/step/coilData')[0].text \
            .replace(';', '').split('\n')
        data = []
        for data_el in data_str:
            if ',' in data_el:
                data.append(float(data_el.split(',')[1]))

        return pd.DataFrame({'x, [mm]': x_strands, 'y, [mm]': y_strands, '|B| (T)': data})

    @staticmethod
    def plotly_results(strand_data: pd.DataFrame, xlim=(0, 80), ylim=(0, 80)) -> None:
        """ Static method plotting results with plotly package

        :param strand_data: a dataframe with strand positions and field values
        :param xlim: limits in x-direction
        :param ylim: limits in y-direction
        """
        roxie = ['rgb(17,0,181)', 'rgb(11,42,238)', 'rgb(0,104,236)', 'rgb(0,154,235)', 'rgb(0,208,226)',
                 'rgb(0,246,244)', 'rgb(0,255,0)', 'rgb(116,255,0)', 'rgb(191,255,0)', 'rgb(252,255,0)',
                 'rgb(255,199,0)', 'rgb(255,146,0)', 'rgb(255,86,0)', 'rgb(255,0,0)', 'rgb(246,0,0)',
                 'rgb(232, 0, 0)', 'rgb(197, 0, 50)', 'rgb(168, 0, 159)']

        fig = px.scatter(strand_data, x="x, [mm]", y="y, [mm]", color="|B| (T)", hover_data=['|B| (T)'],
                         color_continuous_scale=roxie)
        fig.update_layout(autosize=False,
                          width=750,
                          height=600,
                          xaxis_range=xlim,
                          yaxis_range=ylim,
                          plot_bgcolor='rgba(0,0,0,0)',
                          images=[dict(
                              source="https://i.ibb.co/kcc2mbw/ROXIE.png",
                              xref="paper", yref="paper",
                              x=1.16, y=-0.1,
                              sizex=0.2, sizey=0.2,
                              xanchor="right", yanchor="bottom"
                          )])
        fig.show()

    @staticmethod
    def update_force2d_with_field_scaling(roxie_force_input_path: str,
                                          roxie_force_output_path: str,
                                          field: float,
                                          target_field: float) -> None:
        """ Static method scaling ROXIE force with actual and target field

        :param roxie_force_input_path: input path with ROXIE Lorentz force
        :param roxie_force_output_path: output path with ROXIE Lorentz force
        :param field: actual field in tesla
        :param target_field: target field in tesla
        """
        roxie_force_txt = text_file.readlines(roxie_force_input_path)

        # # convert text input to a list of floats
        scaling = (target_field / field) ** 2
        roxie_force = []
        for roxie_force_txt_el in roxie_force_txt:
            row_float = [float(el) for el in roxie_force_txt_el.replace('\n', '').split(' ') if el != '']
            row_float[2] *= scaling
            row_float[3] *= scaling
            roxie_force.append(row_float)

        with open(roxie_force_output_path, 'w') as file_write:
            for roxie_force_el in roxie_force:
                row_str = [str(roxie_force_el_el) for roxie_force_el_el in roxie_force_el]
                file_write.write(' '.join(row_str) + '\n')

    @staticmethod
    def correct_xml_file(input_xml_path: str, output_xml_path: str) -> None:
        """ Static method for correcting an XML file by removing the first empty line and a first space in the second
        line. The corrected XML file is valid and can be automatically parsed.

        :param input_xml_path: path of an input XML file
        :param output_xml_path: path of an output, corrected XML file
        """
        xml_lines = text_file.read(input_xml_path)

        # get rid of an extra first line and a starting empty space in the second line
        if xml_lines[:2] == '\n ':
            xml_lines = xml_lines[2:]

        text_file.write(output_xml_path, xml_lines)


class TerminalRoxieToolAdapter(RoxieToolAdapter):

    def __init__(self,
                 input_folder_rel_dir: str,
                 input_file: str,
                 output_file: str,
                 cadata_file: str,
                 xml_output_file: str,
                 executable_name: str = 'runroxie'
                 ):
        """ Constructor of a TerminalRoxieToolAdapter object

        :param input_folder_rel_dir: a relative path to input folder w.r.t. notebook location
        :param input_file: a name of an input file
        :param output_file: a name of an output file. It is the input file name with .output extension
        :param cadata_file: a name of a cadata file
        :param xml_output_file: a name of an output XML file with plot information from ROXIE
        :param executable_name: name of ROXIE executable, typically runroxie
        """
        super().__init__(input_folder_rel_dir=input_folder_rel_dir,
                         input_file=input_file,
                         output_file=output_file,
                         cadata_file=cadata_file,
                         xml_output_file=xml_output_file)
        self.executable_name = executable_name

    def _get_process_command(self):
        return [self.executable_name, self.input_file_path]


class DockerTerminalRoxieToolAdapter(TerminalRoxieToolAdapter):

    def __init__(self,
                 input_folder_rel_dir: str,
                 input_file: str,
                 output_file: str,
                 cadata_file: str,
                 xml_output_file: str,
                 executable_name: str = 'runroxie',
                 docker_image_name: str = 'roxie_terminal'
                 ):
        """ Constructor of a DockerTerminalRoxieToolAdapter object

        :param input_folder_rel_dir: a relative path to input folder w.r.t. notebook location
        :param input_file: a name of an input file
        :param output_file: a name of an output file. It is the input file name with .output extension
        :param cadata_file: a name of a cadata file
        :param xml_output_file: a name of an output XML file with plot information from ROXIE
        :param executable_name: a name of ROXIE executable, typically runroxie
        :param docker_image_name: a name of ROXIE Docker terminal image executable, typically roxie_terminal
        """
        super().__init__(input_folder_rel_dir=input_folder_rel_dir,
                         input_file=input_file,
                         output_file=output_file,
                         cadata_file=cadata_file,
                         xml_output_file=xml_output_file,
                         executable_name=executable_name)
        self.docker_image_name = docker_image_name
        self.file_to_unlink = os.path.join(input_folder_rel_dir, 'm4_A.inp')

    def run(self):
        super().run()
        self.wait_until_output_exist(timeout_in_sec=10)
        self.unlink_file(self.file_to_unlink)

    def _get_process_command(self):
        if platform.system() == 'Windows':
            input_file_path_temp = self.input_file_path.replace('\\', '/')
        else:
            input_file_path_temp = self.input_file_path

        return ['docker', 'exec', self.docker_image_name, self.executable_name, input_file_path_temp]

    def wait_until_output_exist(self, timeout_in_sec=10) -> None:
        """ Method waiting until an output file exists. The waiting time is given as an argument. In case of a timeout
         a FileNotFoundError is raised

        :param timeout_in_sec: timeout in seconds
        """
        output_file_path_corrected = self.output_file_path.replace('\\', '/')
        count = 0
        while not os.path.isfile(output_file_path_corrected) and count < timeout_in_sec:
            time.sleep(1)
            count += 1

        if not os.path.isfile(output_file_path_corrected):
            raise FileNotFoundError('The file %s does not exist!' % output_file_path_corrected)

    @staticmethod
    def unlink_file(file_path: str) -> None:
        """ Static method unlinking a file that otherwise causes an error in copying files

        :param file_path: a path to a file to unlink
        """
        if platform.system() == 'Windows':
            file_path = file_path.replace('\\', '/')

        try:
            os.unlink(file_path)
        except:
            print('File does not exist' % file_path)
