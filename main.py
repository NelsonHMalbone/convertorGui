import PySimpleGUI as st

# creating the tab layouts
tab1_layout = [[st.Text('File to Compress'), st.InputText(), st.FilesBrowse(key='file_compress')],
               [st.Text('Folder Destination'), st.InputText(), st.FolderBrowse(key='folder_compress')],
               [st.Button('Confirm'), st.Text(key='output', text_color='green')]
               ]

tab2_layout = [[st.T('Unzip File')]]

# creating the layout vars:
# zip_input_text = st.Text('File to Zip')
# zip_input_field = st.InputText()
# zip_input_file = st.FilesBrowse()
# zip_des_text = st.Text('File Des')
# zip_des_field = st.InputText()
# zip_des_file = st.FolderBrowse()
# confirm_btn = st.Button('Confirm')
# output_info = st.Text(key='output', text_color='green')

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
