import PySimpleGUI as sT


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

    layout = [[sT.TabGroup([[sT.Tab('Zip File', tab1_layout, tooltip='to zip files'),
                             sT.Tab('Unzip File', tab2_layout, tooltip='to unzip files')]])]]

    # creating the window
    window = sT.Window('Project Name',
                       layout=layout)

    # event loop to process events and get values of inputs

    while True:
        event, values = window.read()

        # when the user closes or "x's" the window

        if event == sT.WIN_CLOSED or event == 'cancel':
            break

        print('Hello', values[0], '!')


if __name__ == '__main__':
    main()
