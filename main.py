import PySimpleGUI as st

# creating the tab layouts
tab1_layout = [[st.Text('File to Compress: '), st.InputText(), st.FilesBrowse(key='file_compress')],
               [st.Text('Select Destination: '), st.InputText(), st.FolderBrowse(key='folder_compress')],
               [st.Button('Confirm'), st.Text(key='output', text_color='green'), st.Push(), st.Button('Exit', key='Exit')]
               ]

tab2_layout = [[st.Text('Files to archive: '), st.InputText(), st.FilesBrowse(key='files_archive')],
               [st.Text('Select Destination: '), st.InputText(), st.FolderBrowse(key='folder_archive')],
               [st.Button('Confirm'), st.Text(key='output', text_color='green'), st.Push(), st.Button('Exit', key='Exit')]
               ]

layout = [[st.TabGroup([[st.Tab('Zip File', tab1_layout, tooltip='to zip files'),
                         st.Tab('Unzip File', tab2_layout, tooltip='to unzip files')]])]]

# creating the window
window = st.Window('Project Name',
                   layout=layout)

# event loop to process events and get values of inputs

while True:
    event, values = window.read()

    # when the user closes or "x's" the window

    if event == st.WIN_CLOSED or event == 'cancel':
        break

    print('Hello', values[0], '!')

window.close()
