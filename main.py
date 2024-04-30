import PySimpleGUI as sT
from functions import archive


def main():

    # creating the tab layouts
    tab1_layout = [[sT.Text('File to Compress: '), sT.InputText(), sT.FilesBrowse(key='file_compress')],
                   [sT.Text('Select Destination: '), sT.InputText(), sT.FolderBrowse(key='folder_compress')],
                   [sT.Button('Confirm'), sT.Text(key='output', text_color='green'), sT.Push(),
                    sT.Button('Exit', key='Exit')]
                   ]

    tab2_layout = [[sT.Text('Files to archive: '), sT.InputText(), sT.FilesBrowse(key='files_archive')],
                   [sT.Text('Select Destination: '), sT.InputText(), sT.FolderBrowse(key='folder_archive')],
                   [sT.Button('Confirm'), sT.Text(key='output', text_color='green'), sT.Push(),
                    sT.Button('Exit', key='Exit')]
                   ]

    layout = [[sT.TabGroup([[sT.Tab('Zip File', tab1_layout),
                             sT.Tab('Unzip File', tab2_layout)]])]]

    # creating the window
    window = sT.Window('-Zip-',
                       layout=layout)

    # event loop to process events and get values of inputs

    while True:
        # zip files
        event, values = window.read()
        file_path = values['file_compress'].split(';')
        folder_path = values['folder_compress']
        archive(file_path, folder_path)
        window['output'].update(value='Compression Successfully Completed')

        # unzip files

        # when the user pushes the button to close the window
        if event == sT.WIN_CLOSED or event == 'Exit':
            break


if __name__ == '__main__':
    main()
