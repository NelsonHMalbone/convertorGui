import PySimpleGUI as sT
from functions import archive, extraction


def main():
    try:
        # creating the tab layouts
        tab1_layout = [[sT.Text('File to Compress: '), sT.InputText(), sT.FilesBrowse(key='file_compress')],
                       [sT.Text('Select Destination: '), sT.InputText(), sT.FolderBrowse(key='folder_compress')],
                       [sT.Button('Confirm'), sT.Text(key='zipped_output', text_color='green'), sT.Push(),
                        sT.Button('Exit', key='Exit')]
                       ]

        tab2_layout = [[sT.Text('Files to archive: '), sT.InputText(), sT.FilesBrowse(key='files_archive')],
                       [sT.Text('Select Destination: '), sT.InputText(), sT.FolderBrowse(key='folder_archive')],
                       [sT.Button('Confirm'), sT.Text(key='unzip_output', text_color='green'), sT.Push(),
                        sT.Button('Exit', key='Exit')]
                       ]

        layout = [[sT.TabGroup([[sT.Tab('Zip File', tab1_layout),
                                 sT.Tab('Unzip File', tab2_layout)]])]]

        # creating the window
        window = sT.Window('-Zip-',
                           layout=layout)

        # event loop to process events and get values of inputs

        while True:
            try:
                # what the program uses to get data to process:
                event, values = window.read()
                # zip files
                file_path = values['file_compress'].split(';')
                folder_path = values['folder_compress']
                archive(file_path, folder_path)
                window['zipped_output'].update(value='Compression Successfully Completed')

                # unzip files
                archive_path = values['files_archive']
                dest_dir = values['folder_archive']
                extraction(archive_path, dest_dir)
                window['unzip_output'].update(value='Extraction Successfully Completed')
                # when the user pushes the button to close the window
                if event == sT.WIN_CLOSED or event == 'Exit':
                    break
            except FileNotFoundError:
                break

    except AttributeError:
        error = sT.WIN_CLOSED


if __name__ == '__main__':
    main()
