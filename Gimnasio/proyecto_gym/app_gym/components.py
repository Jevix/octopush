from reactpy import component, html, use_state

@component
def login():
    dni_input_value, set_dni_input_value = use_state('')
    contrasena_input_value, set_contrasena_input_value = use_state('')
    input_type, set_input_type = use_state('password')

    def dni_handle_change(event):
        set_dni_input_value(event['target']['value'])

    def contrasena_handle_change(event):
        set_contrasena_input_value(event['target']['value'])

    def toggle_password_visibility(event):
        set_input_type('text' if input_type == 'password' else 'password')

    dni_border_color = 'rgba(0, 0, 0, 1)' if dni_input_value.strip() else 'rgba(0, 0, 0, 0.5)'

    contrasena_border_color = 'rgba(0, 0, 0, 1)' if contrasena_input_value.strip() else 'rgba(0, 0, 0, 0.5)'

    button_color = 'rgba(0, 0, 0, 1)' if dni_input_value.strip() and contrasena_input_value.strip() else 'rgba(0, 0, 0, 0.5)'

    text_color = 'rgba(255, 255, 255, 1)' if dni_input_value.strip() and contrasena_input_value.strip() else 'rgba(0, 0, 0, 1)'
    return html.div({
        "class": "container",
        },

     html.form(
        html.legend("Accede a tu cuenta"),
        html.input({
            "onChange": dni_handle_change,
            "placeholder": "DNI",
            "class": "inputText",
            "style": {'border': f'1px solid {dni_border_color}'}
        }),
        html.div({
            "class": "containerContrasena"
        },
        html.input({
            "type": input_type,
            "onChange": contrasena_handle_change,
            "id": "inputContrasena",
            "placeholder": "Contraseña",
            "class": "inputText",
            "style": {'border': f'1px solid {contrasena_border_color}'}
        }),
        html.button({
            "onClick": toggle_password_visibility,
            "type": "button",
            "class": "iconButton"
        },
            html.i(
                {"class": "bx bx-show bx-md"}
            )
        ),
        ),        

        html.div({
            "class":"containerRecordarme"
        },
            html.input({
                "type": "checkbox",
                "class": "inputCheckBox"
            }),
            html.label("Recordarme"),
        ),
        html.button({
            "class": "buttonLogin",
            "style": {"background-color": button_color, "color": text_color}
        }, "Ingresar")
    ))

@component
def home():
    return html.div(
        html.h1("Home en desarrollo...")
    )