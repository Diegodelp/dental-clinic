from array import array
from ast import Str
from datetime import datetime
from queue import Empty
import pytz
from cgitb import grey, text
from genericpath import exists
from operator import index
from sys import displayhook
from tkinter import *
from tkinter import Menu
from tkinter import filedialog
from tkinter import messagebox
import os
import json
import time
import pathlib
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from turtle import bgcolor, onclick, width
import tkinter.ttk
import tkinter.font as font
from typing_extensions import Self
from click import command
from tkinter import filedialog as fd 
from PIL import ImageTk, Image, ImageDraw
from pydrive.drive import GoogleDrive
from pathlib import Path
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from apiclient.http import MediaFileUpload,MediaIoBaseDownload
import json

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    global creds
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)

        # Call the Drive v3 API
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()


def guardar():

        print(entry_base_input.get())
        pacientes = {"General":{"Paciente":{
                    "Paciente": nombre.get(),
                    "Sexo": sexoStr.get(),
                    "Fecha_Consulta": fecha.get(),
                    "Embarazo": embarazo.get(),
                    "Tratamientos": tratamientos.get(),
                    "Fecha_Nacimiento": edad.get(),
                    "Direccion": direccion.get(),
                    "Telefono": telefono.get(),
                    "Obra_Social": obrasocial.get(),
                    "Observaciones": f"{observaciones.get()}\n" + f"{observaciones2.get()}\n" + f"{observaciones3.get()}\n" f"{observaciones4.get()}\n",
                    "Enf_Respiratorias" : f"{agreementa.get()}, {enfrespiratorias.get()}",
                    "Enf_Cardiacas" : f"{agreementb.get()}, {enfcardiacas.get()}",
                    "Enf_Alergicas" : f"{agreementc.get()}, {enfalegicas.get()}",
                    "Enf_Autoinmunes" : f"{agreementd.get()}, {enfautoinmunes.get()}",
                    "Enf_Renales" : f"{agreemente.get()}, {enfrenales.get()}",
                    "Cirugias_Previas" : f"{agreementf.get()}, {cirugiasprevias.get()}",
                    "Motivo_de_Consulta" : f"{motivoc.get()}",
                            "Dientes":  {
                                "Sector_1":{
                                            "e18": {"Palatino":e18p.get(),
                                                    "Vestibular":e18v.get(),
                                                    "Oclusal":e18o.get(),
                                                    "Mesial":e18m.get(),
                                                    "Distal":e18d.get()},
                                            "e17": {"Palatino":e17p.get(),
                                                    "Vestibular":e17v.get(),
                                                    "Oclusal":e17o.get(),
                                                    "Mesial":e17m.get(),
                                                    "Distal":e17d.get()},
                                            "e16": {"Palatino":e16p.get(),
                                                    "Vestibular":e16v.get(),
                                                    "Oclusal":e16o.get(),
                                                    "Mesial":e16m.get(),
                                                    "Distal":e16d.get()},
                                            "e15": {"Palatino":e15p.get(),
                                                    "Vestibular":e15v.get(),
                                                    "Oclusal":e15o.get(),
                                                    "Mesial":e15m.get(),
                                                    "Distal":e15d.get()},
                                            "e14": {"Palatino":e14p.get(),
                                                    "Vestibular":e14v.get(),
                                                    "Oclusal":e14o.get(),
                                                    "Mesial":e14m.get(),
                                                    "Distal":e14d.get()},
                                            "e13": {"Palatino":e13p.get(),
                                                    "Vestibular":e13v.get(),
                                                    "Oclusal":e13o.get(),
                                                    "Mesial":e13m.get(),
                                                    "Distal":e13d.get()},
                                            "e12": {"Palatino":e12p.get(),
                                                    "Vestibular":e12v.get(),
                                                    "Oclusal":e12o.get(),
                                                    "Mesial":e12m.get(),
                                                    "Distal":e12d.get()},
                                            "e11": {"Palatino":e11p.get(),
                                                    "Vestibular":e11v.get(),
                                                    "Oclusal":e11o.get(),
                                                    "Mesial":e11m.get(),
                                                    "Distal":e11d.get()}
                                            },
                                "Sector_2": {"e28": {"Palatino":e28p.get(),
                                                    "Vestibular":e28v.get(),
                                                    "Oclusal":e28o.get(),
                                                    "Mesial":e28m.get(),
                                                    "Distal":e28d.get()},
                                            "e27": {"Palatino":e27p.get(),
                                                    "Vestibular":e27v.get(),
                                                    "Oclusal":e27o.get(),
                                                    "Mesial":e27m.get(),
                                                    "Distal":e27d.get()},
                                            "e26": {"Palatino":e26p.get(),
                                                    "Vestibular":e26v.get(),
                                                    "Oclusal":e26o.get(),
                                                    "Mesial":e26m.get(),
                                                    "Distal":e26d.get()},
                                            "e25": {"Palatino":e25p.get(),
                                                    "Vestibular":e25v.get(),
                                                    "Oclusal":e25o.get(),
                                                    "Mesial":e25m.get(),
                                                    "Distal":e25d.get()},
                                            "e24": {"Palatino":e24p.get(),
                                                    "Vestibular":e24v.get(),
                                                    "Oclusal":e24o.get(),
                                                    "Mesial":e24m.get(),
                                                    "Distal":e24d.get()},
                                            "e23": {"Palatino":e23p.get(),
                                                    "Vestibular":e23v.get(),
                                                    "Oclusal":e23o.get(),
                                                    "Mesial":e23m.get(),
                                                    "Distal":e23d.get()},
                                            "e22": {"Palatino":e22p.get(),
                                                    "Vestibular":e22v.get(),
                                                    "Oclusal":e22o.get(),
                                                    "Mesial":e22m.get(),
                                                    "Distal":e22d.get()},
                                            "e21": {"Palatino":e21p.get(),
                                                    "Vestibular":e21v.get(),
                                                    "Oclusal":e21o.get(),
                                                    "Mesial":e21m.get(),
                                                    "Distal":e21d.get()}
                                                    },
                                "Sector_3": {"e38": {"Palatino":e38p.get(),
                                                    "Vestibular":e38v.get(),
                                                    "Oclusal":e38o.get(),
                                                    "Mesial":e38m.get(),
                                                    "Distal":e38d.get()},
                                            "e37": {"Palatino":e37p.get(),
                                                    "Vestibular":e37v.get(),
                                                    "Oclusal":e37o.get(),
                                                    "Mesial":e37m.get(),
                                                    "Distal":e37d.get()},
                                            "e36": {"Palatino":e36p.get(),
                                                    "Vestibular":e36v.get(),
                                                    "Oclusal":e36o.get(),
                                                    "Mesial":e36m.get(),
                                                    "Distal":e36d.get()},
                                            "e35": {"Palatino":e35p.get(),
                                                    "Vestibular":e35v.get(),
                                                    "Oclusal":e35o.get(),
                                                    "Mesial":e35m.get(),
                                                    "Distal":e35d.get()},
                                            "e34": {"Palatino":e34p.get(),
                                                    "Vestibular":e34v.get(),
                                                    "Oclusal":e34o.get(),
                                                    "Mesial":e34m.get(),
                                                    "Distal":e34d.get()},
                                            "e33": {"Palatino":e33p.get(),
                                                    "Vestibular":e33v.get(),
                                                    "Oclusal":e33o.get(),
                                                    "Mesial":e33m.get(),
                                                    "Distal":e33d.get()},
                                            "e32": {"Palatino":e32p.get(),
                                                    "Vestibular":e32v.get(),
                                                    "Oclusal":e32o.get(),
                                                    "Mesial":e32m.get(),
                                                    "Distal":e32d.get()},
                                            "e31": {"Palatino":e31p.get(),
                                                    "Vestibular":e31v.get(),
                                                    "Oclusal":e31o.get(),
                                                    "Mesial":e31m.get(),
                                                    "Distal":e31d.get()}
                                                    },
                                "Sector_4": {"e48": {"Palatino":e48p.get(),
                                                    "Vestibular":e48v.get(),
                                                    "Oclusal":e48o.get(),
                                                    "Mesial":e48m.get(),
                                                    "Distal":e48d.get()},
                                            "e47": {"Palatino":e47p.get(),
                                                    "Vestibular":e47v.get(),
                                                    "Oclusal":e47o.get(),
                                                    "Mesial":e47m.get(),
                                                    "Distal":e47d.get()},
                                            "e46": {"Palatino":e46p.get(),
                                                    "Vestibular":e46v.get(),
                                                    "Oclusal":e46o.get(),
                                                    "Mesial":e46m.get(),
                                                    "Distal":e46d.get()},
                                            "e45": {"Palatino":e45p.get(),
                                                    "Vestibular":e45v.get(),
                                                    "Oclusal":e45o.get(),
                                                    "Mesial":e45m.get(),
                                                    "Distal":e45d.get()},
                                            "e44": {"Palatino":e44p.get(),
                                                    "Vestibular":e44v.get(),
                                                    "Oclusal":e44o.get(),
                                                    "Mesial":e44m.get(),
                                                    "Distal":e44d.get()},
                                            "e43": {"Palatino":e43p.get(),
                                                    "Vestibular":e43v.get(),
                                                    "Oclusal":e43o.get(),
                                                    "Mesial":e43m.get(),
                                                    "Distal":e43d.get()},
                                            "e42": {"Palatino":e42p.get(),
                                                    "Vestibular":e42v.get(),
                                                    "Oclusal":e42o.get(),
                                                    "Mesial":e42m.get(),
                                                    "Distal":e42d.get()},
                                            "e41": {"Palatino":e41p.get(),
                                                    "Vestibular":e41v.get(),
                                                    "Oclusal":e41o.get(),
                                                    "Mesial":e41m.get(),
                                                    "Distal":e41d.get()}
                                                    }               
                            },
                        "Fotos":{"Oclusal_Superior":f"http://127.0.0.1:5001/pacientes/image/{oclusals}",
                                "Oclusal_Inferior":f"http://127.0.0.1:5001/pacientes/image/{oclusali}",
                                "Lateral_Izquierda":f"http://127.0.0.1:5001/pacientes/image/{laterali}",
                                "Lateral_Derecha":f"http://127.0.0.1:5001/pacientes/image/{laterald}",
                                "Frente":f"http://127.0.0.1:5001/pacientes/image/{frente}",
                                "Cara":f"http://127.0.0.1:5001/pacientes/image/{cara}",
                                "Perfil_Izquierdo":f"http://127.0.0.1:5001/pacientes/image/{perfili}",
                                "Perfil_Derecho":f"http://127.0.0.1:5001/pacientes/image/{perfild}",
                        },
                        "Diagnostico":{ "Biotipo_Facial":biotipof.get(),
                                        "Habitos_Parafuncionales":habitosp.get(),
                                        "Malposiciones":malposic.get(),
                                        "Alineacion_Interarcada":alinterarc.get(),
                                        "Entrecruzamiento": entrp.get(),
                                        "Linea_Media_Facial": lmediaf.get(),
                                        "Linea_Media_Dentaria":lmediad.get(),
                                        "Overbite":overb.get(),
                                        "Overjet": overjet.get(),
                                        "Curva_Spee": curvas.get(),
                                        "Clase_Molar_Izquierda": clasemi.get(),
                                        "Clase_Molar_Derecha": clasemd.get(),
                                        "Clase_Canina_Izquierda": claseci.get(),
                                        "Clase_Canina_Derecha": clasecd.get(),
                                        "Denticion": dent.get(),
                                        "I_arctemp_Cs": iatempcs.get(),
                                        "I_arctemp_1ms": iatemp1ms.get(),
                                        "I_arctemp_2ms": iatemp2ms.get(),
                                        "I_arctemp_Ci": iatempci.get(),
                                        "I_arctemp_1mi": iatemp1mi.get(),
                                        "I_arctemp_2mi": iatemp2mi.get(),
                                        "I_m_Cs": imcs.get(),
                                        "I_m_1ms": im1ms.get(),
                                        "I_m_2ms": im2ms.get(),
                                        "I_m_Ci": imci.get(),
                                        "I_m_1mi": im1mi.get(),
                                        "I_m_2mi": im2mi.get(),
                                        "I_rick_Cs": irickcs.get(),
                                        "I_rick_1ms": irick1ms.get(),
                                        "I_rick_2ms": irick2ms.get(),
                                        "I_rick_Ci": irickci.get(),
                                        "I_rick_1mi": irick1mi.get(),
                                        "I_rick_2mi": irick2mi.get(),
                                        "Prof_Paladar": profpaladar.get(),
                                        "Discrepancia": discrepancia.get(),
                                        "Relacion_canina": rcanina.get(),
                                        "Relacion_molar": rmolar.get(),
                                        "Angulo_Interincisivo": anginter.get(),
                                        "Convexidad": convexidad.get(),
                                        "Altura_facial": altfaci.get(),
                                        "Protrusion_labial": protrusionl.get(),
                                        "Profundidad_facial": pfacial.get(),
                                        "Eje_facial": ejef.get(),
                                        "Ang_Plano_mandibular": apman.get(),
                                        "Altura_maxilar": amax.get(),
                                        "Profundidad_maxilar": pmax.get(),
                                       
                                        
                        }
        }
        }
        }                   
                                            
                                        
                                
                
        verificar = os.path.exists('./grupopacientes')
        if verificar == True:
            fileName = f"C:/Users/diego/Desktop/ProgrmacionPhyton/consultorio/pacientes/grupopacientes/{nombre.get()}.json"
            isarchivo = os.path.isfile(fileName)
            if isarchivo == True:
                with open(f'grupopacientes/{nombre.get()}.json','w') as document:
                        json.dump(pacientes, document, indent=3)
                        messagebox.showinfo("Informacion","Se ha actualizado el paciente correctamente")
                        print (selected_patologias.get())

            else:
                with open(f'grupopacientes/{nombre.get()}.json','w') as document:
                        json.dump(pacientes, document, indent=3)
                        messagebox.showinfo("Informacion","Se ha añadido el paciente correctamente")

        else:
            directorio = "grupopacientes"
  
            # Parent Directory path
            parent_dir = "C:/Users/diego/Desktop/ProgrmacionPhyton/consultorio/pacientes"
            
            # Path
            path = os.path.join(parent_dir, directorio)
            
            # Create the directory
            # 'GeeksForGeeks' in
            # '/home / User / Documents'
            os.mkdir(path)
            messagebox.showinfo("Informacion","La Carpeta no existia, se ha creado y se ha añadido el Paciente")
            with open(f'grupopacientes/{nombre.get()}.json','w') as document:
                    json.dump(pacientes, document, indent=3)
                    messagebox.showinfo("Informacion","Se ha añadido el paciente correctamente")



def back_to_main():
        global current_frame
        current_frame.pack_forget()
        inicio.pack()
        current_frame = inicio             
    
def show_datos_filiatorios():  
        global current_frame
        current_frame.pack_forget()
        datosfiliatorios_frame.pack()
        current_frame = datosfiliatorios_frame
        
def show_motivo_consulta():
        global current_frame
        current_frame.pack_forget()
        motivoconsulta_frame.pack()
        current_frame = motivoconsulta_frame

def show_antecedentes_patologicos():  
        global current_frame
        current_frame.pack_forget()
        antecedentes_patologicos_frame.pack()
        current_frame = antecedentes_patologicos_frame

def show_odontograma():
        global current_frame
        current_frame.pack_forget()
        odontograma_frame.pack()
        current_frame = odontograma_frame

def show_fotos():
        global current_frame
        current_frame.pack_forget()
        fotos_frame.pack()
        current_frame = fotos_frame

def show_diagnostico():
        global current_frame
        current_frame.pack_forget()
        diagnostico_frame.pack()
        current_frame = diagnostico_frame

def create_datos_filiatorios():
    
        pst = pytz.timezone('America/Argentina/Cordoba')
        global fecha
        fecha = StringVar()
        fecha.set(datetime.date(datetime.now(pst)))
        global nombre
        nombre = StringVar()
        global edad
        edad = StringVar()
        global direccion
        direccion = StringVar()
        global telefono
        telefono = StringVar()
        global obrasocial
        obrasocial = StringVar()
        global sexoStr
        sexoStr = tk.StringVar()
        global tratamientos
        tratamientos = StringVar()
        


        datos_filiatorios = ttk.Button(datosfiliatorios_frame, text="Datos Filiatorios")
        datos_filiatorios.grid(row=0, column=1, pady=5)
        
        label_base_input = ttk.Label(datosfiliatorios_frame,text="Nombre y Apellido")
        label_base_input.grid(row=1, column=1,sticky=W, pady=5)
        global entry_base_input
        entry_base_input = ttk.Entry(datosfiliatorios_frame,textvariable=nombre, width= 21)
        entry_base_input.grid(row=2, column=1,sticky=N,pady=5, padx= 3)
        
        global embarazo
        global embarazoE
        global embarazoL
        embarazo = StringVar()
        embarazo.set('No corresponde')
        global sexo
        def sexo(event):
            if sexoStr.get() == "Femenino":
                global embarazo
                global embarazoE
                global embarazoL       
                embarazo = StringVar()
                embarazo.set('')
                embarazoL = ttk.Label(datosfiliatorios_frame,text=" Embarazo")
                embarazoL.grid(row=15, column=1,sticky=W, pady=5)

                embarazoE = ttk.Entry(datosfiliatorios_frame,textvariable=embarazo, width= 21)
                embarazoE.grid(row=16, column=1,sticky=N,pady=5, padx= 3)
            if sexoStr.get() == "Masculino":
                embarazoL.grid_forget()
                embarazoE.grid_forget()
        
        global sexoE
        sexoL = ttk.Label(datosfiliatorios_frame,text="Sexo")
        sexoL.grid(row=3, column=1,sticky=W, pady=5)
        
        sexoE = ttk.Combobox(datosfiliatorios_frame, textvariable=sexoStr , values=["Masculino", "Femenino"])
        sexoE.bind('<<ComboboxSelected>>', sexo)
        sexoE.grid(row=4,column=1)

        edadL = ttk.Label(datosfiliatorios_frame,text="Fecha de Nacimiento")
        edadL.grid(row=5, column=1,sticky=W, pady=5)

        global edadE
        edadE = ttk.Entry(datosfiliatorios_frame,textvariable=edad, width= 21)
        edadE.grid(row=6, column=1,sticky=N,pady=5, padx= 3)

        
        direccionL = ttk.Label(datosfiliatorios_frame,text=" Direccion")
        direccionL.grid(row=7, column=1,sticky=W, pady=5)
        global direccionE
        direccionE = ttk.Entry(datosfiliatorios_frame,textvariable=direccion, width= 21)
        direccionE.grid(row=8, column=1,sticky=N,pady=5, padx= 3)

        telefonoL = ttk.Label(datosfiliatorios_frame,text=" Telefono")
        telefonoL.grid(row=9, column=1,sticky=W, pady=5)
        global telefonoE
        telefonoE = ttk.Entry(datosfiliatorios_frame,textvariable=telefono, width= 21)
        telefonoE.grid(row=10, column=1,sticky=N,pady=5, padx= 3)

        obrasocialL = ttk.Label(datosfiliatorios_frame,text=" Obra Social")
        obrasocialL.grid(row=11, column=1,sticky=W, pady=5)

        global obrasocialE
        obrasocialE = ttk.Entry(datosfiliatorios_frame,textvariable=obrasocial, width= 21)
        obrasocialE.grid(row=12, column=1,sticky=N,pady=5, padx= 3)

        fechaL = ttk.Label(datosfiliatorios_frame,text=" Fecha de Ingreso")
        fechaL.grid(row=13, column=1,sticky=W, pady=5)

        global fechaE
        fechaE = ttk.Entry(datosfiliatorios_frame,textvariable=fecha, width= 21)
        fechaE.grid(row=14, column=1,sticky=N,pady=5, padx= 3)

        tratamientosL = ttk.Label(datosfiliatorios_frame,text=" Tratamientos")
        tratamientosL.grid(row=17, column=1,sticky=W, pady=5)

        global tratamientosE
        tratamientosE = ttk.Entry(datosfiliatorios_frame,textvariable=tratamientos, width= 21)
        tratamientosE.grid(row=18, column=1,sticky=N,pady=5, padx= 3)
        

        
        

        ttk.Button(datosfiliatorios_frame, text="Back", command=back_to_main).grid(row=19,column=1,sticky=N,pady=5, padx= 3)

        return nombre

def create_motivo_consulta():
            #Motivo de Consulta
        global motivoc
        motivoc = StringVar()

        motivo_de_consultaTitle = ttk.Button(motivoconsulta_frame, text="---------------------")
        motivo_de_consultaTitle.grid(row=0, column=3, sticky=W, pady=5)

        motivo_de_consultaL = ttk.Label(motivoconsulta_frame, text="Motivo de consulta")
        motivo_de_consultaL.grid(row=1, column=3, sticky=W, pady=5)

        global motivo_de_consultaE
        motivo_de_consultaE = ttk.Entry(motivoconsulta_frame,textvariable=motivoc, width= 21,)
        motivo_de_consultaE.grid(row=2, column=3,sticky=N,pady=5, padx= 3)

        ttk.Button(motivoconsulta_frame, text="Back", command=back_to_main).grid(row=11,column=3,sticky=S,pady=5, padx= 3)


def create_antecedentes_patologicos():
        global agreementa
        agreementa = tk.StringVar()
        agreementa.set('No')
        global agreementb
        agreementb = tk.StringVar()
        agreementb.set('No')
        global agreementc
        agreementc = tk.StringVar()
        agreementc.set('No')
        global agreementd
        agreementd = tk.StringVar()
        agreementd.set('No')
        global agreemente
        agreemente = tk.StringVar()
        agreemente.set('No')
        global agreementf
        agreementf = tk.StringVar()
        agreementf.set('No')

        enfermedades = ttk.Button(antecedentes_patologicos_frame, text="Enfermedades Previas")
        enfermedades.grid(row=0, column=4, pady=5)

        global enfrespiratorias
        global enfcardiacas
        global enfautoinmunes
        global enfrenales
        global enfalegicas
        global cirugiasprevias    

        label_base_input = ttk.Label(antecedentes_patologicos_frame,text=" Enf. Respiratorias")
        label_base_input.grid(row=1, column=4,sticky=W,pady=10)
        a = ttk.Checkbutton(antecedentes_patologicos_frame,
                        command=agreementa,
                        variable=agreementa,
                        onvalue='Si',
                        offvalue='No',
                         ).grid(row=1, column=5,sticky=W)

        enfrespiratorias = StringVar()
        global addEntrya
        addEntrya = ttk.Entry(antecedentes_patologicos_frame,textvariable=enfrespiratorias, width= 21)
        addEntrya.grid(row=2, column=4,sticky=S, pady=5, padx= 3)

        #Añadir Enf. Cardiacas

        label_base_input = ttk.Label(antecedentes_patologicos_frame,text=" Enf. Cardiacas")
        label_base_input.grid(row=3, column=4,sticky=W,pady=10)
        b = ttk.Checkbutton(antecedentes_patologicos_frame,
                        command=agreementb,
                        variable=agreementb,
                        onvalue='Si',
                        offvalue='No',
                        ).grid(row=3, column=5,sticky=W)

        enfcardiacas = StringVar()
        global addEntryb
        addEntryb = ttk.Entry(antecedentes_patologicos_frame,textvariable=enfcardiacas, width= 21)
        addEntryb.grid(row=4, column=4,sticky=S, pady=5, padx= 3)

        #Añadir Enf. Alergicas

        label_base_input = ttk.Label(antecedentes_patologicos_frame,text=" Enf. Alergicas")
        label_base_input.grid(row=5, column=4,sticky=W,pady=5)
        c = ttk.Checkbutton(antecedentes_patologicos_frame,
                        command=agreementc,
                        variable=agreementc,
                        onvalue='Si',
                        offvalue='No',
                         ).grid(row=5, column=5,sticky=W)

        enfalegicas = StringVar()
        global addEntryc
        addEntryc = ttk.Entry(antecedentes_patologicos_frame,textvariable=enfalegicas, width= 21)
        addEntryc.grid(row=6, column=4,sticky=S, pady=5, padx= 3)

        #Añadir Enf. Autoinmunes 

        label_base_input = ttk.Label(antecedentes_patologicos_frame,text=" Enf. Autoinmunes")
        label_base_input.grid(row=7, column=4,sticky=W, pady=10)
        d = ttk.Checkbutton(antecedentes_patologicos_frame,
                        command=agreementd,
                        variable=agreementd,
                        onvalue='Si',
                        offvalue='No',
                         ).grid(row=7, column=5,sticky=W)

        enfautoinmunes = StringVar()
        global addEntryd
        addEntryd = ttk.Entry(antecedentes_patologicos_frame,textvariable=enfautoinmunes, width= 21)
        addEntryd.grid(row=8, column=4,sticky=S, pady=5, padx= 3)

        #Añadir Enf. Renales

        label_base_input = ttk.Label(antecedentes_patologicos_frame,text=" Enf. Renales")
        label_base_input.grid(row=9, column=4,sticky=W, pady=10)
        e = ttk.Checkbutton(antecedentes_patologicos_frame,
                        command=agreemente,
                        variable=agreemente,
                        onvalue='Si',
                        offvalue='No',
                         ).grid(row=9, column=5,sticky=W)
        
        enfrenales = StringVar()
        global addEntrye
        addEntrye = ttk.Entry(antecedentes_patologicos_frame,textvariable=enfrenales, width= 21)
        addEntrye.grid(row=10, column=4,sticky=S, pady=5, padx= 3)

        #Añadir Cirugias Previas

        label_base_input = ttk.Label(antecedentes_patologicos_frame,text=" Cirugias Previas")
        label_base_input.grid(row=11, column=4,sticky=W, pady=10)
        f = ttk.Checkbutton(antecedentes_patologicos_frame,
                        command=agreementf,
                        variable=agreementf,
                        onvalue='Si',
                        offvalue='No',
                         ).grid(row=11, column=5,sticky=W)
        
        cirugiasprevias = StringVar()
        global addEntryf
        addEntryf = ttk.Entry(antecedentes_patologicos_frame,textvariable=cirugiasprevias, width= 21)
        addEntryf.grid(row=12, column=4,sticky=S, pady=5, padx= 3)    

        ttk.Button(antecedentes_patologicos_frame, text="Back", command=back_to_main).grid(row=13,column=4,sticky=N,pady=5, padx= 3)



def create_odontograma():
    #Odontograma
        def cambiar18d():
            e18d.set(selected_patologias.get())
        def cambiar18o():
            e18o.set(selected_patologias.get())
        def cambiar18m():
            e18m.set(selected_patologias.get())
        def cambiar18v():
            e18v.set(selected_patologias.get())      
        def cambiar18p():
            e18p.set(selected_patologias.get())

        global selected_patologias
        global selected_p
        selected_patologias = tk.StringVar()
        patologias = ttk.Combobox(odontograma_frame, text=selected_patologias, values=["Caries", "Endodoncia", "Exodoncia", "Corona", "Puente","Obturacion"])
        patologias.grid(row=10,column=37)


        global e18d
        global e18o
        global e18m
        global e18v
        global e18p
        e18c = 'white'
        e18d = tk.StringVar()
        e18d.set('Sano')   
        e18o = tk.StringVar()
        e18o.set('Sano')
        e18m = tk.StringVar()
        e18m.set('Sano')
        e18v = tk.StringVar()
        e18v.set('Sano')
        e18p = tk.StringVar()
        e18p.set('Sano')

        elemento18L = ttk.Label(odontograma_frame, text="18")
        elemento18L.grid(column=7, row=1)
        elemento18D = ttk.Checkbutton(odontograma_frame, width=0 ,onvalue=e18o, text='',command=cambiar18d)
        elemento18D.grid(column=6, row=3)
        elemento18O = ttk.Checkbutton(odontograma_frame, width=0,onvalue=e18o, text='',command=cambiar18o)
        elemento18O.grid(column=7, row=3, padx= 1)
        elemento18M = ttk.Checkbutton(odontograma_frame, width=0,onvalue=e18m, text='',command=cambiar18m)
        elemento18M.grid(column=8, row=3)
        elemento18V = ttk.Checkbutton(odontograma_frame, width=0,onvalue=e18v, text='',command=cambiar18v)
        elemento18V.grid(column=7, row=2)
        elemento18P = ttk.Checkbutton(odontograma_frame, width=0,onvalue=e18p, text='',command=cambiar18p)
        elemento18P.grid(column=7, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=9,row=2, rowspan=3, sticky='ns', padx= 3)

        def cambiar17d():
            e17d.set(selected_patologias.get())
        def cambiar17o():
            e17o.set(selected_patologias.get())
        def cambiar17m():
            e17m.set(selected_patologias.get())
        def cambiar17v():
            e17v.set(selected_patologias.get())      
        def cambiar17p():
            e17p.set(selected_patologias.get())

        global e17d
        global e17o
        global e17m
        global e17v
        global e17p
        
        e17d = tk.StringVar()
        e17d.set('Sano')
        e17o = tk.StringVar()
        e17o.set('Sano')
        e17m = tk.StringVar()
        e17m.set('Sano')
        e17v = tk.StringVar()
        e17v.set('Sano')
        e17p = tk.StringVar()
        e17p.set('Sano')

        elemento17L = ttk.Label(odontograma_frame, text="17")
        elemento17L.grid(column=11, row=1)

        elemento17D = ttk.Checkbutton(odontograma_frame, width=0,onvalue=e17d, text='',command=cambiar17d)
        elemento17D.grid(column=10, row=3)
        elemento17O = ttk.Checkbutton(odontograma_frame, width=0,onvalue=e17o, text='',command=cambiar17o)
        elemento17O.grid(column=11, row=3, padx= 3)
        elemento17M = ttk.Checkbutton(odontograma_frame, width=0,onvalue=e17m, text='',command=cambiar17m)
        elemento17M.grid(column=12, row=3, )
        elemento17V = ttk.Checkbutton(odontograma_frame, width=0,onvalue=e17v, text='',command=cambiar17v)
        elemento17V.grid(column=11, row=2)
        elemento17P = ttk.Checkbutton(odontograma_frame, width=0,onvalue=e17p, text='',command=cambiar17p)
        elemento17P.grid(column=11, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=13,row=2, rowspan=3, sticky='ns', padx= 3)

        def cambiar16d():
            e16d.set(selected_patologias.get())
        def cambiar16o():
            e16o.set(selected_patologias.get())
        def cambiar16m():
            e16m.set(selected_patologias.get())
        def cambiar16v():
            e16v.set(selected_patologias.get())      
        def cambiar16p():
            e16p.set(selected_patologias.get())

        global e16d
        global e16o
        global e16m
        global e16v
        global e16p
        
        e16d = tk.StringVar()
        e16d.set('Sano')
        e16o = tk.StringVar()
        e16o.set('Sano')
        e16m = tk.StringVar()
        e16m.set('Sano')
        e16v = tk.StringVar()
        e16v.set('Sano')
        e16p = tk.StringVar()
        e16p.set('Sano')

        elemento16L = ttk.Label(odontograma_frame, text="16")
        elemento16L.grid(column=15, row=1)

        elemento16D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar16d)
        elemento16D.grid(column=14, row=3)
        elemento16O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar16o)
        elemento16O.grid(column=15, row=3, padx= 3)
        elemento16M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar16m)
        elemento16M.grid(column=16, row=3)
        elemento16V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar16v)
        elemento16V.grid(column=15, row=2)
        elemento16P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar16p)
        elemento16P.grid(column=15, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=17,row=2, rowspan=3, sticky='ns', padx= 3)

        def cambiar15d():
            e15d.set(selected_patologias.get())
        def cambiar15o():
            e15o.set(selected_patologias.get())
        def cambiar15m():
            e15m.set(selected_patologias.get())
        def cambiar15v():
            e15v.set(selected_patologias.get())      
        def cambiar15p():
            e15p.set(selected_patologias.get())

        global e15d
        global e15o
        global e15m
        global e15v
        global e15p
        
        e15d = tk.StringVar()
        e15d.set('Sano')
        e15o = tk.StringVar()
        e15o.set('Sano')
        e15m = tk.StringVar()
        e15m.set('Sano')
        e15v = tk.StringVar()
        e15v.set('Sano')
        e15p = tk.StringVar()
        e15p.set('Sano')    

        elemento15L = ttk.Label(odontograma_frame, text="15")
        elemento15L.grid(column=19, row=1)

        elemento15D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar15d)
        elemento15D.grid(column=18, row=3)
        elemento15O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar15o)
        elemento15O.grid(column=19, row=3, padx= 3)
        elemento15M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar15m)
        elemento15M.grid(column=20, row=3)
        elemento15V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar15v)
        elemento15V.grid(column=19, row=2)
        elemento15P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar15p)
        elemento15P.grid(column=19, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=21,row=2, rowspan=3, sticky='ns', padx= 3)

        def cambiar14d():
            e14d.set(selected_patologias.get())
        def cambiar14o():
            e14o.set(selected_patologias.get())
        def cambiar14m():
            e14m.set(selected_patologias.get())
        def cambiar14v():
            e14v.set(selected_patologias.get())      
        def cambiar14p():
            e14p.set(selected_patologias.get())

        

        global e14d
        global e14o
        global e14m
        global e14v
        global e14p
        
        e14d = tk.StringVar()
        e14o = tk.StringVar()
        e14m = tk.StringVar()
        e14v = tk.StringVar()
        e14p = tk.StringVar()
        e14d.set('Sano')
        e14o.set('Sano')
        e14m.set('Sano')
        e14v.set('Sano')
        e14p.set('Sano')

        elemento14L = ttk.Label(odontograma_frame, text="14")
        elemento14L.grid(column=23, row=1)

        elemento14D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar14d)
        elemento14D.grid(column=22, row=3)
        elemento14O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar14o)
        elemento14O.grid(column=23, row=3, padx= 3)
        elemento14M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar14m)
        elemento14M.grid(column=24, row=3)
        elemento14V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar14v)
        elemento14V.grid(column=23, row=2)
        elemento14P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar14p)
        elemento14P.grid(column=23, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=25,row=2, rowspan=3, sticky='ns', padx= 3)

        def cambiar13d():
            e13d.set(selected_patologias.get())
        def cambiar13o():
            e13o.set(selected_patologias.get())
        def cambiar13m():
            e13m.set(selected_patologias.get())
        def cambiar13v():
            e13v.set(selected_patologias.get())      
        def cambiar13p():
            e13p.set(selected_patologias.get())

        global e13d
        global e13o
        global e13m
        global e13v
        global e13p
        
        e13d = tk.StringVar()
        e13o = tk.StringVar()
        e13m = tk.StringVar()
        e13v = tk.StringVar()
        e13p = tk.StringVar()
        e13d.set('Sano')
        e13o.set('Sano')
        e13m.set('Sano')
        e13v.set('Sano')
        e13p.set('Sano')

        elemento13L = ttk.Label(odontograma_frame, text="13")
        elemento13L.grid(column=27, row=1)

        elemento13D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar13d)
        elemento13D.grid(column=26, row=3)
        elemento13O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar13o)
        elemento13O.grid(column=27, row=3, padx= 3)
        elemento13M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar13m)
        elemento13M.grid(column=28, row=3)
        elemento13V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar13v)
        elemento13V.grid(column=27, row=2)
        elemento13P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar13p)
        elemento13P.grid(column=27, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=29,row=2, rowspan=3, sticky='ns', padx= 3)

        def cambiar12d():
            e12d.set(selected_patologias.get())
        def cambiar12o():
            e12o.set(selected_patologias.get())
        def cambiar12m():
            e12m.set(selected_patologias.get())
        def cambiar12v():
            e12v.set(selected_patologias.get())      
        def cambiar12p():
            e12p.set(selected_patologias.get())

        global e12d
        global e12o
        global e12m
        global e12v
        global e12p
        
        e12d = tk.StringVar()
        e12o = tk.StringVar()
        e12m = tk.StringVar()
        e12v = tk.StringVar()
        e12p = tk.StringVar()
        e12d.set('Sano')
        e12o.set('Sano')
        e12m.set('Sano')
        e12v.set('Sano')
        e12p.set('Sano')

        elemento12L = ttk.Label(odontograma_frame, text="12")
        elemento12L.grid(column=31, row=1)

        elemento12D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar12d)
        elemento12D.grid(column=30, row=3)
        elemento12O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar12o)
        elemento12O.grid(column=31, row=3, padx= 3)
        elemento12M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar12m)
        elemento12M.grid(column=32, row=3)
        elemento12V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar12v)
        elemento12V.grid(column=31, row=2)
        elemento12P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar12p)
        elemento12P.grid(column=31, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=33,row=2, rowspan=3, sticky='ns', padx= 3)

        def cambiar11d():
            e11d.set(selected_patologias.get())
        def cambiar11o():
            e11o.set(selected_patologias.get())
        def cambiar11m():
            e11m.set(selected_patologias.get())
        def cambiar11v():
            e11v.set(selected_patologias.get())      
        def cambiar11p():
            e11p.set(selected_patologias.get())

        global e11d
        global e11o
        global e11m
        global e11v
        global e11p
        
        e11d = tk.StringVar()
        e11o = tk.StringVar()
        e11m = tk.StringVar()
        e11v = tk.StringVar()
        e11p = tk.StringVar()
        e11d.set('Sano')
        e11o.set('Sano')
        e11m.set('Sano')
        e11v.set('Sano')
        e11p.set('Sano')

        elemento11L = ttk.Label(odontograma_frame, text="11")
        elemento11L.grid(column=35, row=1)

        elemento11D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar11d)
        elemento11D.grid(column=34, row=3)
        elemento11O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar11o)
        elemento11O.grid(column=35, row=3, padx= 3)
        elemento11M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar11m)
        elemento11M.grid(column=36, row=3)
        elemento11V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar11v)
        elemento11V.grid(column=35, row=2)
        elemento11P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar11p)
        elemento11P.grid(column=35, row=4)

        #Sector 2

        def cambiar21d():
            e21d.set(selected_patologias.get())
        def cambiar21o():
            e21o.set(selected_patologias.get())
        def cambiar21m():
            e21m.set(selected_patologias.get())
        def cambiar21v():
            e21v.set(selected_patologias.get())      
        def cambiar21p():
            e21p.set(selected_patologias.get())

        global e21d
        global e21o
        global e21m
        global e21v
        global e21p
        
        e21d = tk.StringVar()
        e21o = tk.StringVar()
        e21m = tk.StringVar()
        e21v = tk.StringVar()
        e21p = tk.StringVar()
        e21d.set('Sano')
        e21o.set('Sano')
        e21m.set('Sano')
        e21v.set('Sano')
        e21p.set('Sano')

        elemento21L = ttk.Label(odontograma_frame, text="21")
        elemento21L.grid(column=41, row=1)


        elemento21M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar21d)
        elemento21M.grid(column=40, row=3)
        elemento21O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar21o)
        elemento21O.grid(column=41, row=3, padx= 3)
        elemento21D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar21m)
        elemento21D.grid(column=42, row=3)
        elemento21V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar21v)
        elemento21V.grid(column=41, row=2)
        elemento21P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar21p)
        elemento21P.grid(column=41, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=43,row=2, rowspan=3, sticky='ns', padx= 3)

        def cambiar22d():
            e22d.set(selected_patologias.get())
        def cambiar22o():
            e22o.set(selected_patologias.get())
        def cambiar22m():
            e22m.set(selected_patologias.get())
        def cambiar22v():
            e22v.set(selected_patologias.get())      
        def cambiar22p():
            e22p.set(selected_patologias.get())

        global e22d
        global e22o
        global e22m
        global e22v
        global e22p
        
        e22d = tk.StringVar()
        e22o = tk.StringVar()
        e22m = tk.StringVar()
        e22v = tk.StringVar()
        e22p = tk.StringVar()
        e22d.set('Sano')
        e22o.set('Sano')
        e22m.set('Sano')
        e22v.set('Sano')
        e22p.set('Sano')

        elemento22L = ttk.Label(odontograma_frame, text="22")
        elemento22L.grid(column=45, row=1)


        elemento22M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar22d)
        elemento22M.grid(column=44, row=3)
        elemento22O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar22o)
        elemento22O.grid(column=45, row=3, padx= 3)
        elemento22D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar22m)
        elemento22D.grid(column=46, row=3)
        elemento22V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar22v)
        elemento22V.grid(column=45, row=2)
        elemento22P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar22p)
        elemento22P.grid(column=45, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=47,row=2, rowspan=3, sticky='ns', padx= 3)

        def cambiar23d():
            e23d.set(selected_patologias.get())
        def cambiar23o():
            e23o.set(selected_patologias.get())
        def cambiar23m():
            e23m.set(selected_patologias.get())
        def cambiar23v():
            e23v.set(selected_patologias.get())      
        def cambiar23p():
            e23p.set(selected_patologias.get())

        global e23d
        global e23o
        global e23m
        global e23v
        global e23p
        
        e23d = tk.StringVar()
        e23o = tk.StringVar()
        e23m = tk.StringVar()
        e23v = tk.StringVar()
        e23p = tk.StringVar()
        e23d.set('Sano')
        e23o.set('Sano')
        e23m.set('Sano')
        e23v.set('Sano')
        e23p.set('Sano')

        elemento23L = ttk.Label(odontograma_frame, text="23")
        elemento23L.grid(column=50, row=1)


        elemento23M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar23d)
        elemento23M.grid(column=49, row=3)
        elemento23O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar23o)
        elemento23O.grid(column=50, row=3, padx= 3)
        elemento23D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar23m)
        elemento23D.grid(column=51, row=3)
        elemento23V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar23v)
        elemento23V.grid(column=50, row=2)
        elemento23P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar23p)
        elemento23P.grid(column=50, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=52,row=2, rowspan=3, sticky='ns', padx= 3)

        def cambiar24d():
            e24d.set(selected_patologias.get())
        def cambiar24o():
            e24o.set(selected_patologias.get())
        def cambiar24m():
            e24m.set(selected_patologias.get())
        def cambiar24v():
            e24v.set(selected_patologias.get())      
        def cambiar24p():
            e24p.set(selected_patologias.get())

        global e24d
        global e24o
        global e24m
        global e24v
        global e24p
        
        e24d = tk.StringVar()
        e24o = tk.StringVar()
        e24m = tk.StringVar()
        e24v = tk.StringVar()
        e24p = tk.StringVar()
        e24d.set('Sano')
        e24o.set('Sano')
        e24m.set('Sano')
        e24v.set('Sano')
        e24p.set('Sano')

        elemento24L = ttk.Label(odontograma_frame, text="24")
        elemento24L.grid(column=54, row=1)


        elemento24M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar24d)
        elemento24M.grid(column=53, row=3)
        elemento24O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar24o)
        elemento24O.grid(column=54, row=3, padx= 3)
        elemento24D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar24m)
        elemento24D.grid(column=55, row=3)
        elemento24V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar24v)
        elemento24V.grid(column=54, row=2)
        elemento24P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar24p)
        elemento24P.grid(column=54, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=56,row=2, rowspan=3, sticky='ns', padx= 3)

        def cambiar25d():
            e25d.set(selected_patologias.get())
        def cambiar25o():
            e25o.set(selected_patologias.get())
        def cambiar25m():
            e25m.set(selected_patologias.get())
        def cambiar25v():
            e25v.set(selected_patologias.get())      
        def cambiar25p():
            e25p.set(selected_patologias.get())

        global e25d
        global e25o
        global e25m
        global e25v
        global e25p
        
        e25d = tk.StringVar()
        e25o = tk.StringVar()
        e25m = tk.StringVar()
        e25v = tk.StringVar()
        e25p = tk.StringVar()
        e25d.set('Sano')
        e25o.set('Sano')
        e25m.set('Sano')
        e25v.set('Sano')
        e25p.set('Sano')

        elemento25L = ttk.Label(odontograma_frame, text="25")
        elemento25L.grid(column=58, row=1)


        elemento25M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar25d)
        elemento25M.grid(column=57, row=3)
        elemento25O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar25o)
        elemento25O.grid(column=58, row=3, padx= 3)
        elemento25D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar25m)
        elemento25D.grid(column=59, row=3)
        elemento25V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar25v)
        elemento25V.grid(column=58, row=2)
        elemento25P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar25p)
        elemento25P.grid(column=58, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=60,row=2, rowspan=3, sticky='ns', padx= 3)

        def cambiar26d():
            e26d.set(selected_patologias.get())
        def cambiar26o():
            e26o.set(selected_patologias.get())
        def cambiar26m():
            e26m.set(selected_patologias.get())
        def cambiar26v():
            e26v.set(selected_patologias.get())      
        def cambiar26p():
            e26p.set(selected_patologias.get())

        global e26d
        global e26o
        global e26m
        global e26v
        global e26p
        
        e26d = tk.StringVar()
        e26o = tk.StringVar()
        e26m = tk.StringVar()
        e26v = tk.StringVar()
        e26p = tk.StringVar()
        e26d.set('Sano')
        e26o.set('Sano')
        e26m.set('Sano')
        e26v.set('Sano')
        e26p.set('Sano')

        elemento26L = ttk.Label(odontograma_frame, text="26")
        elemento26L.grid(column=62, row=1)


        elemento26M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar26d)
        elemento26M.grid(column=61, row=3)
        elemento26O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar26o)
        elemento26O.grid(column=62, row=3, padx= 3)
        elemento26D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar26m)
        elemento26D.grid(column=63, row=3)
        elemento26V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar26v)
        elemento26V.grid(column=62, row=2)
        elemento26P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar26p)
        elemento26P.grid(column=62, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=64,row=2, rowspan=3, sticky='ns', padx= 3)

        def cambiar27d():
            e27d.set(selected_patologias.get())
        def cambiar27o():
            e27o.set(selected_patologias.get())
        def cambiar27m():
            e27m.set(selected_patologias.get())
        def cambiar27v():
            e27v.set(selected_patologias.get())      
        def cambiar27p():
            e27p.set(selected_patologias.get())

        global e27d
        global e27o
        global e27m
        global e27v
        global e27p
        
        e27d = tk.StringVar()
        e27o = tk.StringVar()
        e27m = tk.StringVar()
        e27v = tk.StringVar()
        e27p = tk.StringVar()
        e27d.set('Sano')
        e27o.set('Sano')
        e27m.set('Sano')
        e27v.set('Sano')
        e27p.set('Sano')

        elemento27L = ttk.Label(odontograma_frame, text="27")
        elemento27L.grid(column=66, row=1)


        elemento27M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar27d)
        elemento27M.grid(column=65, row=3)
        elemento27O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar27o)
        elemento27O.grid(column=66, row=3, padx= 3)
        elemento27D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar27m)
        elemento27D.grid(column=67, row=3)
        elemento27V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar27v)
        elemento27V.grid(column=66, row=2)
        elemento27P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar27p)
        elemento27P.grid(column=66, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=68,row=2, rowspan=3, sticky='ns', padx= 3)

        def cambiar28d():
            e28d.set(selected_patologias.get())
        def cambiar28o():
            e28o.set(selected_patologias.get())
        def cambiar28m():
            e28m.set(selected_patologias.get())
        def cambiar28v():
            e28v.set(selected_patologias.get())      
        def cambiar28p():
            e28p.set(selected_patologias.get())

        global e28d
        global e28o
        global e28m
        global e28v
        global e28p
        
        e28d = tk.StringVar()
        e28o = tk.StringVar()
        e28m = tk.StringVar()
        e28v = tk.StringVar()
        e28p = tk.StringVar()
        e28d.set('Sano')
        e28o.set('Sano')
        e28m.set('Sano')
        e28v.set('Sano')
        e28p.set('Sano')

        elemento28L = ttk.Label(odontograma_frame, text="28")
        elemento28L.grid(column=70, row=1)


        elemento28M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar28d)
        elemento28M.grid(column=69, row=3)
        elemento28O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar28o)
        elemento28O.grid(column=70, row=3, padx= 3)
        elemento28D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar28m)
        elemento28D.grid(column=71, row=3)
        elemento28V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar28v)
        elemento28V.grid(column=70, row=2)
        elemento28P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar28p)
        elemento28P.grid(column=70, row=4)

        def cambiar48d():
            e48d.set(selected_patologias.get())
        def cambiar48o():
            e48o.set(selected_patologias.get())
        def cambiar48m():
            e48m.set(selected_patologias.get())
        def cambiar48v():
            e48v.set(selected_patologias.get())      
        def cambiar48p():
            e48p.set(selected_patologias.get())

        global e48d
        global e48o
        global e48m
        global e48v
        global e48p
        
        e48d = tk.StringVar()
        e48o = tk.StringVar()
        e48m = tk.StringVar()
        e48v = tk.StringVar()
        e48p = tk.StringVar()
        e48d.set('Sano')
        e48o.set('Sano')
        e48m.set('Sano')
        e48v.set('Sano')
        e48p.set('Sano')

        elemento48L = ttk.Label(odontograma_frame, text="48")
        elemento48L.grid(column=7, row=5)

        elemento48D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar48d)
        elemento48D.grid(column=6, row=7)
        elemento48O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar48o)
        elemento48O.grid(column=7, row=7, padx= 3)
        elemento48M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar48m)
        elemento48M.grid(column=8, row=7)
        elemento48P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar48p)
        elemento48P.grid(column=7, row=6)
        elemento48V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar48v)
        elemento48V.grid(column=7, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=9,row=6, rowspan=3, sticky='ns', padx= 3)

        def cambiar47d():
            e47d.set(selected_patologias.get())
        def cambiar47o():
            e47o.set(selected_patologias.get())
        def cambiar47m():
            e47m.set(selected_patologias.get())
        def cambiar47v():
            e47v.set(selected_patologias.get())      
        def cambiar47p():
            e47p.set(selected_patologias.get())

        global e47d
        global e47o
        global e47m
        global e47v
        global e47p
        
        e47d = tk.StringVar()
        e47o = tk.StringVar()
        e47m = tk.StringVar()
        e47v = tk.StringVar()
        e47p = tk.StringVar()
        e47d.set('Sano')
        e47o.set('Sano')
        e47m.set('Sano')
        e47v.set('Sano')
        e47p.set('Sano')

        elemento47L = ttk.Label(odontograma_frame, text="47")
        elemento47L.grid(column=11, row=5)

        elemento47D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar47d)
        elemento47D.grid(column=10, row=7)
        elemento47O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar47o)
        elemento47O.grid(column=11, row=7, padx= 3)
        elemento47M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar47m)
        elemento47M.grid(column=12, row=7, )
        elemento47P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar47p)
        elemento47P.grid(column=11, row=6)
        elemento47V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar47v)
        elemento47V.grid(column=11, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=13,row=6, rowspan=3, sticky='ns', padx= 3)

        def cambiar46d():
            e46d.set(selected_patologias.get())
        def cambiar46o():
            e46o.set(selected_patologias.get())
        def cambiar46m():
            e46m.set(selected_patologias.get())
        def cambiar46v():
            e46v.set(selected_patologias.get())      
        def cambiar46p():
            e46p.set(selected_patologias.get())

        global e46d
        global e46o
        global e46m
        global e46v
        global e46p
        
        e46d = tk.StringVar()
        e46o = tk.StringVar()
        e46m = tk.StringVar()
        e46v = tk.StringVar()
        e46p = tk.StringVar()
        e46d.set('Sano')
        e46o.set('Sano')
        e46m.set('Sano')
        e46v.set('Sano')
        e46p.set('Sano')

        elemento46L = ttk.Label(odontograma_frame, text="46")
        elemento46L.grid(column=15, row=5)

        elemento46D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar46d)
        elemento46D.grid(column=14, row=7)
        elemento46O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar46o)
        elemento46O.grid(column=15, row=7, padx= 3)
        elemento46M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar46m)
        elemento46M.grid(column=16, row=7)
        elemento46P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar46p)
        elemento46P.grid(column=15, row=6)
        elemento46V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar46v)
        elemento46V.grid(column=15, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=17,row=6, rowspan=3, sticky='ns', padx= 3)

        def cambiar45d():
            e45d.set(selected_patologias.get())
        def cambiar45o():
            e45o.set(selected_patologias.get())
        def cambiar45m():
            e45m.set(selected_patologias.get())
        def cambiar45v():
            e45v.set(selected_patologias.get())      
        def cambiar45p():
            e45p.set(selected_patologias.get())

        global e45d
        global e45o
        global e45m
        global e45v
        global e45p
        
        e45d = tk.StringVar()
        e45o = tk.StringVar()
        e45m = tk.StringVar()
        e45v = tk.StringVar()
        e45p = tk.StringVar()
        e45d.set('Sano')
        e45o.set('Sano')
        e45m.set('Sano')
        e45v.set('Sano')
        e45p.set('Sano')

        elemento45L = ttk.Label(odontograma_frame, text="45")
        elemento45L.grid(column=19, row=5)

        elemento45D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar45d)
        elemento45D.grid(column=18, row=7)
        elemento45O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar45o)
        elemento45O.grid(column=19, row=7, padx= 3)
        elemento45M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar45m)
        elemento45M.grid(column=20, row=7)
        elemento45P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar45p)
        elemento45P.grid(column=19, row=6)
        elemento45V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar45v)
        elemento45V.grid(column=19, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=21,row=6, rowspan=3, sticky='ns', padx= 3)

        def cambiar44d():
            e44d.set(selected_patologias.get())
        def cambiar44o():
            e44o.set(selected_patologias.get())
        def cambiar44m():
            e44m.set(selected_patologias.get())
        def cambiar44v():
            e44v.set(selected_patologias.get())      
        def cambiar44p():
            e44p.set(selected_patologias.get())

        global e44d
        global e44o
        global e44m
        global e44v
        global e44p
        
        e44d = tk.StringVar()
        e44o = tk.StringVar()
        e44m = tk.StringVar()
        e44v = tk.StringVar()
        e44p = tk.StringVar()
        e44d.set('Sano')
        e44o.set('Sano')
        e44m.set('Sano')
        e44v.set('Sano')
        e44p.set('Sano')

        elemento44L = ttk.Label(odontograma_frame, text="44")
        elemento44L.grid(column=23, row=5)

        elemento44D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar44d)
        elemento44D.grid(column=22, row=7)
        elemento44O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar44o)
        elemento44O.grid(column=23, row=7, padx= 3)
        elemento44M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar44m)
        elemento44M.grid(column=24, row=7)
        elemento44P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar44p)
        elemento44P.grid(column=23, row=6)
        elemento44V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar44v)
        elemento44V.grid(column=23, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=25,row=6, rowspan=3, sticky='ns', padx= 3)

        def cambiar43d():
            e43d.set(selected_patologias.get())
        def cambiar43o():
            e43o.set(selected_patologias.get())
        def cambiar43m():
            e43m.set(selected_patologias.get())
        def cambiar43v():
            e43v.set(selected_patologias.get())      
        def cambiar43p():
            e43p.set(selected_patologias.get())

        global e43d
        global e43o
        global e43m
        global e43v
        global e43p
        
        e43d = tk.StringVar()
        e43o = tk.StringVar()
        e43m = tk.StringVar()
        e43v = tk.StringVar()
        e43p = tk.StringVar()
        e43d.set('Sano')
        e43o.set('Sano')
        e43m.set('Sano')
        e43v.set('Sano')
        e43p.set('Sano')

        elemento43L = ttk.Label(odontograma_frame, text="43")
        elemento43L.grid(column=27, row=5)

        elemento43D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar43d)
        elemento43D.grid(column=26, row=7)
        elemento43O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar43o)
        elemento43O.grid(column=27, row=7, padx= 3)
        elemento43M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar43m)
        elemento43M.grid(column=28, row=7)
        elemento43P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar43p)
        elemento43P.grid(column=27, row=6)
        elemento43V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar43v)
        elemento43V.grid(column=27, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=29,row=6, rowspan=3, sticky='ns', padx= 3)

        def cambiar42d():
            e42d.set(selected_patologias.get())
        def cambiar42o():
            e42o.set(selected_patologias.get())
        def cambiar42m():
            e42m.set(selected_patologias.get())
        def cambiar42v():
            e42v.set(selected_patologias.get())      
        def cambiar42p():
            e42p.set(selected_patologias.get())

        global e42d
        global e42o
        global e42m
        global e42v
        global e42p
        
        e42d = tk.StringVar()
        e42o = tk.StringVar()
        e42m = tk.StringVar()
        e42v = tk.StringVar()
        e42p = tk.StringVar()
        e42d.set('Sano')
        e42o.set('Sano')
        e42m.set('Sano')
        e42v.set('Sano')
        e42p.set('Sano')

        elemento42L = ttk.Label(odontograma_frame, text="42")
        elemento42L.grid(column=31, row=5)

        elemento42D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar42d)
        elemento42D.grid(column=30, row=7)
        elemento42O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar42o)
        elemento42O.grid(column=31, row=7, padx= 3)
        elemento42M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar42m)
        elemento42M.grid(column=32, row=7)
        elemento42P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar42p)
        elemento42P.grid(column=31, row=6)
        elemento42V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar42v)
        elemento42V.grid(column=31, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=33,row=6, rowspan=3, sticky='ns', padx= 3)

        def cambiar41d():
            e41d.set(selected_patologias.get())
        def cambiar41o():
            e41o.set(selected_patologias.get())
        def cambiar41m():
            e41m.set(selected_patologias.get())
        def cambiar41v():
            e41v.set(selected_patologias.get())      
        def cambiar41p():
            e41p.set(selected_patologias.get())

        global e41d
        global e41o
        global e41m
        global e41v
        global e41p
        
        e41d = tk.StringVar()
        e41o = tk.StringVar()
        e41m = tk.StringVar()
        e41v = tk.StringVar()
        e41p = tk.StringVar()
        e41d.set('Sano')
        e41o.set('Sano')
        e41m.set('Sano')
        e41v.set('Sano')
        e41p.set('Sano')

        elemento41L = ttk.Label(odontograma_frame, text="41")
        elemento41L.grid(column=35, row=5)

        elemento41D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar41d)
        elemento41D.grid(column=34, row=7)
        elemento41O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar41o)
        elemento41O.grid(column=35, row=7, padx= 3)
        elemento41M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar41m)
        elemento41M.grid(column=36, row=7)
        elemento41P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar41p)
        elemento41P.grid(column=35, row=6)
        elemento41V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar41v)
        elemento41V.grid(column=35, row=8)

        #Sector 3

        def cambiar31d():
            e31d.set(selected_patologias.get())
        def cambiar31o():
            e31o.set(selected_patologias.get())
        def cambiar31m():
            e31m.set(selected_patologias.get())
        def cambiar31v():
            e31v.set(selected_patologias.get())      
        def cambiar31p():
            e31p.set(selected_patologias.get())

        global e31d
        global e31o
        global e31m
        global e31v
        global e31p
        
        e31d = tk.StringVar()
        e31o = tk.StringVar()
        e31m = tk.StringVar()
        e31v = tk.StringVar()
        e31p = tk.StringVar()
        e31d.set('Sano')
        e31o.set('Sano')
        e31m.set('Sano')
        e31v.set('Sano')
        e31p.set('Sano')

        elemento31L = ttk.Label(odontograma_frame, text="31")
        elemento31L.grid(column=41, row=5)


        elemento31M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar31d)
        elemento31M.grid(column=40, row=7)
        elemento31O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar31o)
        elemento31O.grid(column=41, row=7, padx= 3)
        elemento31D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar31m)
        elemento31D.grid(column=42, row=7)
        elemento31P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar31p)
        elemento31P.grid(column=41, row=6)
        elemento31V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar31v)
        elemento31V.grid(column=41, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=43,row=6, rowspan=3, sticky='ns', padx= 3)

        def cambiar32d():
            e32d.set(selected_patologias.get())
        def cambiar32o():
            e32o.set(selected_patologias.get())
        def cambiar32m():
            e32m.set(selected_patologias.get())
        def cambiar32v():
            e32v.set(selected_patologias.get())      
        def cambiar32p():
            e32p.set(selected_patologias.get())

        global e32d
        global e32o
        global e32m
        global e32v
        global e32p
        
        e32d = tk.StringVar()
        e32o = tk.StringVar()
        e32m = tk.StringVar()
        e32v = tk.StringVar()
        e32p = tk.StringVar()
        e32d.set('Sano')
        e32o.set('Sano')
        e32m.set('Sano')
        e32v.set('Sano')
        e32p.set('Sano')

        elemento32L = ttk.Label(odontograma_frame, text="32")
        elemento32L.grid(column=45, row=5)


        elemento32M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar32d)
        elemento32M.grid(column=44, row=7)
        elemento32O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar32o)
        elemento32O.grid(column=45, row=7, padx= 3)
        elemento32D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar32m)
        elemento32D.grid(column=46, row=7)
        elemento32P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar32p)
        elemento32P.grid(column=45, row=6)
        elemento32V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar32v)
        elemento32V.grid(column=45, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=47,row=6, rowspan=3, sticky='ns', padx= 3)

        def cambiar33d():
            e33d.set(selected_patologias.get())
        def cambiar33o():
            e33o.set(selected_patologias.get())
        def cambiar33m():
            e33m.set(selected_patologias.get())
        def cambiar33v():
            e33v.set(selected_patologias.get())      
        def cambiar33p():
            e33p.set(selected_patologias.get())

        global e33d
        global e33o
        global e33m
        global e33v
        global e33p
        
        e33d = tk.StringVar()
        e33o = tk.StringVar()
        e33m = tk.StringVar()
        e33v = tk.StringVar()
        e33p = tk.StringVar()
        e33d.set('Sano')
        e33o.set('Sano')
        e33m.set('Sano')
        e33v.set('Sano')
        e33p.set('Sano')

        elemento33L = ttk.Label(odontograma_frame, text="33")
        elemento33L.grid(column=50, row=5)


        elemento33M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar33d)
        elemento33M.grid(column=49, row=7)
        elemento33O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar33o)
        elemento33O.grid(column=50, row=7, padx= 3)
        elemento33D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar33m)
        elemento33D.grid(column=51, row=7)
        elemento33P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar33p)
        elemento33P.grid(column=50, row=6)
        elemento33V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar33v)
        elemento33V.grid(column=50, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=52,row=6, rowspan=3, sticky='ns', padx= 3)

        def cambiar34d():
            e34d.set(selected_patologias.get())
        def cambiar34o():
            e34o.set(selected_patologias.get())
        def cambiar34m():
            e34m.set(selected_patologias.get())
        def cambiar34v():
            e34v.set(selected_patologias.get())      
        def cambiar34p():
            e34p.set(selected_patologias.get())

        global e34d
        global e34o
        global e34m
        global e34v
        global e34p
        
        e34d = tk.StringVar()
        e34o = tk.StringVar()
        e34m = tk.StringVar()
        e34v = tk.StringVar()
        e34p = tk.StringVar()
        e34d.set('Sano')
        e34o.set('Sano')
        e34m.set('Sano')
        e34v.set('Sano')
        e34p.set('Sano')

        elemento34L = ttk.Label(odontograma_frame, text="34")
        elemento34L.grid(column=54, row=5)


        elemento34M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar34d)
        elemento34M.grid(column=53, row=7)
        elemento34O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar34o)
        elemento34O.grid(column=54, row=7, padx= 3)
        elemento34D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar34m)
        elemento34D.grid(column=55, row=7)
        elemento34P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar34p)
        elemento34P.grid(column=54, row=6)
        elemento34V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar34v)
        elemento34V.grid(column=54, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=56,row=6, rowspan=3, sticky='ns', padx= 3)

        def cambiar35d():
            e35d.set(selected_patologias.get())
        def cambiar35o():
            e35o.set(selected_patologias.get())
        def cambiar35m():
            e35m.set(selected_patologias.get())
        def cambiar35v():
            e35v.set(selected_patologias.get())      
        def cambiar35p():
            e35p.set(selected_patologias.get())

        global e35d
        global e35o
        global e35m
        global e35v
        global e35p
        
        e35d = tk.StringVar()
        e35o = tk.StringVar()
        e35m = tk.StringVar()
        e35v = tk.StringVar()
        e35p = tk.StringVar()
        e35d.set('Sano')
        e35o.set('Sano')
        e35m.set('Sano')
        e35v.set('Sano')
        e35p.set('Sano')

        elemento35L = ttk.Label(odontograma_frame, text="35")
        elemento35L.grid(column=58, row=5)


        elemento35M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar35d)
        elemento35M.grid(column=57, row=7)
        elemento35O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar35o)
        elemento35O.grid(column=58, row=7, padx= 3)
        elemento35D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar35m)
        elemento35D.grid(column=59, row=7)
        elemento35P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar35p)
        elemento35P.grid(column=58, row=6)
        elemento35V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar35v)
        elemento35V.grid(column=58, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=60,row=6, rowspan=3, sticky='ns', padx= 3)

        def cambiar36d():
            e36d.set(selected_patologias.get())
        def cambiar36o():
            e36o.set(selected_patologias.get())
        def cambiar36m():
            e36m.set(selected_patologias.get())
        def cambiar36v():
            e36v.set(selected_patologias.get())      
        def cambiar36p():
            e36p.set(selected_patologias.get())

        global e36d
        global e36o
        global e36m
        global e36v
        global e36p
        
        e36d = tk.StringVar()
        e36o = tk.StringVar()
        e36m = tk.StringVar()
        e36v = tk.StringVar()
        e36p = tk.StringVar()
        e36d.set('Sano')
        e36o.set('Sano')
        e36m.set('Sano')
        e36v.set('Sano')
        e36p.set('Sano')

        elemento36L = ttk.Label(odontograma_frame, text="36")
        elemento36L.grid(column=62, row=5)


        elemento36M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar36d)
        elemento36M.grid(column=61, row=7)
        elemento36O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar36o)
        elemento36O.grid(column=62, row=7, padx= 3)
        elemento36D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar36m)
        elemento36D.grid(column=63, row=7)
        elemento36P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar36p)
        elemento36P.grid(column=62, row=6)
        elemento36V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar36v)
        elemento36V.grid(column=62, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=64,row=6, rowspan=3, sticky='ns', padx= 3)

        def cambiar37d():
            e37d.set(selected_patologias.get())
        def cambiar37o():
            e37o.set(selected_patologias.get())
        def cambiar37m():
            e37m.set(selected_patologias.get())
        def cambiar37v():
            e37v.set(selected_patologias.get())      
        def cambiar37p():
            e37p.set(selected_patologias.get())

        global e37d
        global e37o
        global e37m
        global e37v
        global e37p
        
        e37d = tk.StringVar()
        e37o = tk.StringVar()
        e37m = tk.StringVar()
        e37v = tk.StringVar()
        e37p = tk.StringVar()
        e37d.set('Sano')
        e37o.set('Sano')
        e37m.set('Sano')
        e37v.set('Sano')
        e37p.set('Sano')

        elemento37L = ttk.Label(odontograma_frame, text="37")
        elemento37L.grid(column=66, row=5)


        elemento37M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar37d)
        elemento37M.grid(column=65, row=7)
        elemento37O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar37o)
        elemento37O.grid(column=66, row=7, padx= 3)
        elemento37D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar37m)
        elemento37D.grid(column=67, row=7)
        elemento37P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar37p)
        elemento37P.grid(column=66, row=6)
        elemento37V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar37v)
        elemento37V.grid(column=66, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=68,row=6, rowspan=3, sticky='ns', padx= 3)

        def cambiar38d():
            e38d.set(selected_patologias.get())
        def cambiar38o():
            e38o.set(selected_patologias.get())
        def cambiar38m():
            e38m.set(selected_patologias.get())
        def cambiar38v():
            e38v.set(selected_patologias.get())      
        def cambiar38p():
            e38p.set(selected_patologias.get())

        global e38d
        global e38o
        global e38m
        global e38v
        global e38p
        
        e38d = tk.StringVar()
        e38o = tk.StringVar()
        e38m = tk.StringVar()
        e38v = tk.StringVar()
        e38p = tk.StringVar()
        e38d.set('Sano')
        e38o.set('Sano')
        e38m.set('Sano')
        e38v.set('Sano')
        e38p.set('Sano')

        elemento38L = ttk.Label(odontograma_frame, text="38")
        elemento38L.grid(column=70, row=5)


        elemento38M = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar38d)
        elemento38M.grid(column=69, row=7)
        elemento38O = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar38o)
        elemento38O.grid(column=70, row=7, padx= 3)
        elemento38D = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar38m)
        elemento38D.grid(column=71, row=7)
        elemento38P = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar38p)
        elemento38P.grid(column=70, row=6)
        elemento38V = ttk.Checkbutton(odontograma_frame, width=0, command=cambiar38v)
        elemento38V.grid(column=70, row=8)

        

 
        
        
        
        
        
        global observaciones
        global observaciones2
        global observaciones3
        global observaciones4
        Observaciones_str = StringVar()
        text_observacionesL = ttk.Label(odontograma_frame, text=f"Observacion 1")
        observaciones = tk.Entry(odontograma_frame, width=30, textvariable=Observaciones_str)
        text_observacionesL.grid(row=15, column=37)
        observaciones.grid(row=16, column=37)
        Observaciones_str2 = StringVar()
        text_observacionesL2 = ttk.Label(odontograma_frame, text=f"Observacion 2")
        observaciones2 = tk.Entry(odontograma_frame, width=30, textvariable=Observaciones_str2)
        text_observacionesL2.grid(row=17, column=37)
        observaciones2.grid(row=18, column=37)
        Observaciones_str3 = StringVar()
        text_observacionesL3 = ttk.Label(odontograma_frame, text=f"Observacion 3")
        observaciones3 = tk.Entry(odontograma_frame, width=30, textvariable=Observaciones_str3)
        text_observacionesL3.grid(row=19, column=37)
        observaciones3.grid(row=20, column=37)    
        Observaciones_str4 = StringVar()
        Observaciones_str4.set('')
        observaciones4 = tk.Entry(odontograma_frame, width=30, textvariable=Observaciones_str4)
        
        
        def agregar():
            x = 3
            ob = x
            ob+=1
            global observaciones4
            Observaciones_str4 = StringVar()
            text_observacionesL4 = ttk.Label(odontograma_frame, text=f"Observacion{ob}")
            observaciones4 = tk.Entry(odontograma_frame, width=30, textvariable=Observaciones_str4)
            text_observacionesL4.grid(row=21, column=37)
            observaciones4.grid(row=22, column=37)


            
                
                        

                        
                    
                    
            
                  
                

                
                
                   
                
                
        agregarobservacionB = ttk.Button(odontograma_frame, text="Agregar Observacion", command=agregar)
        agregarobservacionB.grid(row=12, column=37, pady=5)
 
        
        
        

       

        ttk.Button(odontograma_frame, text="Guardar", command=guardar).grid(row=999,pady=5, column=37)
        ttk.Button(odontograma_frame, text="Back", command=back_to_main).grid(row=1000,column=37,sticky=N,pady=5, padx= 3)

def create_fotos():
    lista = []
    global oclusals, oclusali, laterald, laterali, frente, cara, perfili, perfild
    oclusals = ""
    oclusali = ""
    laterali = ""
    laterald = ""
    frente = ""
    cara = ""
    perfild = ""
    perfili = ""

    def open_file():
        global path1
        path1 = "None"
        filename = fd.askopenfilename(initialdir="/", title='Please select a picture to analyze')
        path1 = Path(filename)
        lista.append(path1.name)
        global a1
        label1 = ttk.Label(fotos_frame, text=path1.name)
        label1.grid(row=0, column=2, padx=3)
        arch1 = pathlib.PureWindowsPath(path1)
        str(arch1)
        global oclusals
        oclusals = str(path1.name)
    def open_file2():
        global path2
        path2 = "None"
        filename2 = fd.askopenfilename(initialdir="/", title='Please select a picture to analyze')
        path2 = Path(filename2)
        lista.append(path2.name)
        label2 = ttk.Label(fotos_frame, text=path2.name)
        label2.grid(row=1, column=2, padx=3)
        arch2 = pathlib.PureWindowsPath(path2)
        str(arch2)
        global oclusali
        oclusali = str(path2.name)
    def open_file3():
        global path3
        path3 = "None"
        filename3 = fd.askopenfilename(initialdir="/", title='Please select a picture to analyze')
        path3 = Path(filename3)
        lista.append(path3.name)
        label3 = ttk.Label(fotos_frame, text=path3.name)
        label3.grid(row=2, column=2, padx=3)
        arch3 = pathlib.PureWindowsPath(path3)
        str(arch3)
        global laterali
        laterali = str(path3.name)
    def open_file4():
        global path4
        path4 = "None"
        filename4 = fd.askopenfilename(initialdir="/", title='Please select a picture to analyze')
        path4 = Path(filename4)
        lista.append(path4.name)
        label4 = ttk.Label(fotos_frame, text=path4.name)
        label4.grid(row=3, column=2, padx=3)
        arch4 = pathlib.PureWindowsPath(path4)
        str(arch4)
        global laterald
        laterald = str(path4.name)
    def open_file5():
        global path5
        path5 = "None"
        filename5 = fd.askopenfilename(initialdir="/", title='Please select a picture to analyze')
        path5 = Path(filename5)
        lista.append(path5.name)
        label5 = ttk.Label(fotos_frame, text=path5.name)
        label5.grid(row=4, column=2, padx=3)
        arch5 = pathlib.PureWindowsPath(path5)
        str(arch5)
        global frente
        frente = str(path5.name)
    def open_file6():
        global path6
        path6 = "None"
        filename6 = fd.askopenfilename(initialdir="/", title='Please select a picture to analyze')
        path6 = Path(filename6)
        lista.append(path6.name)    
        label6 = ttk.Label(fotos_frame, text=path6.name)
        label6.grid(row=5, column=2, padx=3)
        arch6 = pathlib.PureWindowsPath(path6)
        str(arch6)
        global cara
        cara = str(path6.name)
    def open_file7():
        global path7
        path7 = "None"
        filename7 = fd.askopenfilename(initialdir="/", title='Please select a picture to analyze')
        path7 = Path(filename7)
        lista.append(path7.name)    
        label7 = ttk.Label(fotos_frame, text=path7.name)
        label7.grid(row=6, column=2, padx=3)
        arch7 = pathlib.PureWindowsPath(path7)
        str(arch7)
        global perfili
        perfili = str(path7.name)
    def open_file8():
        global path8
        path8 = "None"
        filename8 = fd.askopenfilename(initialdir="/", title='Please select a picture to analyze')
        path8 = Path(filename8)
        lista.append(path8.name)    
        label8 = ttk.Label(fotos_frame, text=path8.name)
        label8.grid(row=7, column=2, padx=3)
        arch8 = pathlib.PureWindowsPath(path8)
        str(arch8)
        global perfild
        perfild = str(path8.name)

    
    
            

    def uploadFiles():
        if not lista:
               tk.messagebox.showerror(title="Error", message="No has seleccionado ninguna foto")
        else:
            pb1 = ttk.Progressbar(fotos_frame, orient=HORIZONTAL, length=300, mode='determinate')
            pb1.grid(row=4, columnspan=3)
            for i in range(5):
                fotos_frame.update_idletasks()
                pb1['value'] += 20
                time.sleep(1)
            pb1.destroy()
            service = build('drive', 'v3', credentials=creds)

            folder_metadata = {'name': nombre.get(),'mimeType': 'application/vnd.google-apps.folder'
            }
            folder= service.files().create(body=folder_metadata,fields='id').execute()
            print ('Folder ID: %s' % folder.get('id'))
            folder_id = folder.get('id')

            file_metadata = {'name': path1.name,'parents': [folder_id]}
            media = MediaFileUpload(path1,mimetype='image/', resumable=True)
            file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

            file_metadata2 = {'name': path2.name,'parents': [folder_id]}
            media2 = MediaFileUpload(path2,mimetype='image/', resumable=True)
            file2 = service.files().create(body=file_metadata2, media_body=media2, fields='id').execute()

            file_metadata3 = {'name': path3.name,'parents': [folder_id]}
            media3 = MediaFileUpload(path3,mimetype='image/', resumable=True)
            file3 = service.files().create(body=file_metadata3, media_body=media3, fields='id').execute()

            file_metadata4 = {'name': path4.name,'parents': [folder_id]}
            media4 = MediaFileUpload(path4,mimetype='image/', resumable=True)
            file4 = service.files().create(body=file_metadata4, media_body=media4, fields='id').execute()

            file_metadata5 = {'name': path5.name,'parents': [folder_id]}
            media5 = MediaFileUpload(path4,mimetype='image/', resumable=True)
            file5 = service.files().create(body=file_metadata5, media_body=media5, fields='id').execute()

            file_metadata6 = {'name': path6.name,'parents': [folder_id]}
            media6 = MediaFileUpload(path6,mimetype='image/', resumable=True)
            file6 = service.files().create(body=file_metadata6, media_body=media6, fields='id').execute()

            file_metadata7 = {'name': path7.name,'parents': [folder_id]}
            media7 = MediaFileUpload(path7,mimetype='image/', resumable=True)
            file7 = service.files().create(body=file_metadata7, media_body=media7, fields='id').execute()

            file_metadata8 = {'name': path8.name,'parents': [folder_id]}
            media8 = MediaFileUpload(path8,mimetype='image/', resumable=True)
            file8 = service.files().create(body=file_metadata8, media_body=media8, fields='id').execute()

            

            
            print ('File ID: %s' % file.get('id'))

    
   
           
    
    
    adhar = ttk.Label(fotos_frame, text='Fotos Oclusal Superior (JPG) ')
    adhar.grid(row=0, column=0, padx=10)

    adharbtn = ttk.Button(fotos_frame, text ='Choose File', command = lambda:open_file()) 
    adharbtn.grid(row=0, column=1)

    label1 = ttk.Label(fotos_frame, text="...")
    label1.grid(row=0, column=2, padx=3)

    adhar2 = ttk.Label(fotos_frame, text='Fotos Oclusal Inferior (JPG) ')
    adhar2.grid(row=1, column=0, padx=10)

    adharbtn2 = ttk.Button(fotos_frame, text ='Choose File', command = lambda:open_file2()) 
    adharbtn2.grid(row=1, column=1)

    label2 = ttk.Label(fotos_frame, text="...")
    label2.grid(row=1, column=2, padx=3)

    adhar3 = ttk.Label(fotos_frame, text='Fotos Lateral Izquierda (JPG) ')
    adhar3.grid(row=2, column=0, padx=10)

    adharbtn3 = ttk.Button(fotos_frame, text ='Choose File', command = lambda:open_file3()) 
    adharbtn3.grid(row=2, column=1)

    label3 = ttk.Label(fotos_frame, text="...")
    label3.grid(row=2, column=2, padx=3)

    adhar4 = ttk.Label(fotos_frame, text='Fotos Lateral Derecha (JPG) ')
    adhar4.grid(row=3, column=0, padx=10)

    adharbtn4 = ttk.Button(fotos_frame, text ='Choose File', command = lambda:open_file4()) 
    adharbtn4.grid(row=3, column=1)

    label4 = ttk.Label(fotos_frame, text="...")
    label4.grid(row=3, column=2, padx=3)

    adhar5 = ttk.Label(fotos_frame, text='Fotos Frente (JPG) ')
    adhar5.grid(row=4, column=0, padx=10)

    adharbtn5 = ttk.Button(fotos_frame, text ='Choose File', command = lambda:open_file5()) 
    adharbtn5.grid(row=4, column=1)

    label5 = ttk.Label(fotos_frame, text="...")
    label5.grid(row=4, column=2, padx=3)

    adhar6 = ttk.Label(fotos_frame, text='Fotos de Cara (JPG) ')
    adhar6.grid(row=5, column=0, padx=10)

    adharbtn6 = ttk.Button(fotos_frame, text ='Choose File', command = lambda:open_file6()) 
    adharbtn6.grid(row=5, column=1)

    label6 = ttk.Label(fotos_frame, text="...")
    label6.grid(row=5, column=2, padx=3)

    adhar7 = ttk.Label(fotos_frame, text='Fotos de perfil izquierdo (JPG) ')
    adhar7.grid(row=6, column=0, padx=10)

    adharbtn7 = ttk.Button(fotos_frame, text ='Choose File', command = lambda:open_file7()) 
    adharbtn7.grid(row=6, column=1)

    label7 = ttk.Label(fotos_frame, text="...")
    label7.grid(row=6, column=2, padx=3)

    adhar8 = ttk.Label(fotos_frame, text='Fotos de perfil dereho (JPG) ')
    adhar8.grid(row=7, column=0, padx=10)

    adharbtn8 = ttk.Button(fotos_frame, text ='Choose File', command = lambda:open_file8()) 
    adharbtn8.grid(row=7, column=1)

    label8 = ttk.Label(fotos_frame, text="...")
    label8.grid(row=7, column=2, padx=3)

    upld = ttk.Button(fotos_frame, text='Upload Files', command=uploadFiles)
    upld.grid(row=8, columnspan=3, pady=10)

    ttk.Button(fotos_frame, text="Back", command=back_to_main).grid(row=19,columnspan=3,pady=5)

def create_diagnostico():
    global biotipof, malposic,habitosp,alinterarc
    titulop = ttk.Label(diagnostico_frame, text='General', font=23).grid(pady=5, column=3, row=0)
    biotipof = StringVar()
    biotipo_facialL = ttk.Label(diagnostico_frame, text='Biotipo Facial')
    biotipo_facialL.grid(column=2, row=1)
    biotipo_facialE = ttk.Combobox(diagnostico_frame, textvariable=biotipof, values=["Braquicefalico", "Dolicocefalico", "Normocefalico"])
    biotipo_facialE.grid(column=2, row=2)
    habitosp = StringVar()
    habitospL = ttk.Label(diagnostico_frame, text='Habitos Parafuncionales')
    habitospL.grid(column=4, row=1)
    habitospE = ttk.Entry(diagnostico_frame, textvariable=habitosp)
    habitospE.grid(column=4, row=2)
    malposic = StringVar()
    malposicL = ttk.Label(diagnostico_frame, text='Malposiciones Dentarias')
    malposicL.grid(column=2, row=3)
    malposicE = ttk.Entry(diagnostico_frame, textvariable=malposic)
    malposicE.grid(column=2, row=4)
    alinterarc = StringVar()
    alinterarcL = ttk.Label(diagnostico_frame, text='Alteraciones Interarcadas')
    alinterarcL.grid(column=4, row=3)
    alinterarcE = ttk.Entry(diagnostico_frame, textvariable=alinterarc)
    alinterarcE.grid(column=4, row=4)
    
    titulo1 = ttk.Label(diagnostico_frame, text='Relacion Frontal').grid(pady=5, column=3, row=5)

    global entrp, lmediaf, lmediad
    entrp = StringVar()
    entrpL = ttk.Label(diagnostico_frame, text='Entrecruzamiento Periferico')
    entrpL.grid(column=2, row=6)
    entrpE = ttk.Combobox(diagnostico_frame, textvariable=entrp , values=["Normal", "Invertido"])
    entrpE.grid(column=2, row=7)
    lmediaf = StringVar()
    lmediafL = ttk.Label(diagnostico_frame, text='Linea Media Facial')
    lmediafL.grid(column=3, row=6)
    lmediafE = ttk.Combobox(diagnostico_frame, textvariable=lmediaf , values=["Normal", "Desviada"])
    lmediafE.grid(column=3, row=7)
    lmediad = StringVar()
    lmediadL = ttk.Label(diagnostico_frame, text='Linea Media Dentaria')
    lmediadL.grid(column=4, row=6)
    lmediadE = ttk.Combobox(diagnostico_frame, textvariable=lmediad , values=["Normal", "Desviada"])
    lmediadE.grid(column=4, row=7)
    
    titulo2 = ttk.Label(diagnostico_frame, text='Relacion Veritcal').grid(pady=5, column=3, row=10)

    global overb
    overb = StringVar()
    overbL = ttk.Label(diagnostico_frame, text='Overbite')
    overbL.grid(column=2, row=11)
    overbE = ttk.Combobox(diagnostico_frame, textvariable=overb , values=["Aumentado", "Normal", "Disminuido"])
    overbE.grid(column=2, row=12)

    titulo3 = ttk.Label(diagnostico_frame, text='Relacion Sagital').grid(pady=5, column=3, row=15)
    global overjet,curvas,clasemi,clasemd,claseci,clasecd
    overjet = StringVar()
    overjetL = ttk.Label(diagnostico_frame, text='Overjet')
    overjetL.grid(column=2, row=16)
    overjetE = ttk.Combobox(diagnostico_frame, textvariable=overjet , values=["Aumentado", "Normal", "Disminuido"])
    overjetE.grid(column=2, row=17)
    curvas = StringVar()
    curvasL = ttk.Label(diagnostico_frame, text='Curva de Spee')
    curvasL.grid(column=3, row=16)
    curvasE = ttk.Combobox(diagnostico_frame, textvariable=curvas , values=["Aumentada", "Normal", "Disminuida"])
    curvasE.grid(column=3, row=17)
    clasemi = StringVar()
    clasemiL = ttk.Label(diagnostico_frame, text='Clase Molar Izquierda')
    clasemiL.grid(column=4, row=16)
    clasemiE = ttk.Combobox(diagnostico_frame, textvariable=clasemi , values=["Clase 1", "Clase 2", "Clase 3"])
    clasemiE.grid(column=4, row=17)
    clasemd = StringVar()
    clasemdL = ttk.Label(diagnostico_frame, text='Clase Molar Derecha')
    clasemdL.grid(column=4, row=18)
    clasemdE = ttk.Combobox(diagnostico_frame, textvariable=clasemd , values=["Clase 1", "Clase 2", "Clase 3"])
    clasemdE.grid(column=4, row=19)
    claseci = StringVar()
    claseciL = ttk.Label(diagnostico_frame, text='Clase Canina Izquierda')
    claseciL.grid(column=5, row=16)
    claseciE = ttk.Combobox(diagnostico_frame, textvariable=claseci , values=["Clase 1", "Clase 2", "Clase 3"])
    claseciE.grid(column=5, row=17)
    clasecd = StringVar()
    clasecdL = ttk.Label(diagnostico_frame, text='Clase Canina Derecha')
    clasecdL.grid(column=5, row=18)
    clasecdE = ttk.Combobox(diagnostico_frame, textvariable=clasecd , values=["Clase 1", "Clase 2", "Clase 3"])
    clasecdE.grid(column=5, row=19)

    titulodo = ttk.Label(diagnostico_frame, text='Diagnostico Ortodoncico', font=23).grid(pady=10, column=1, row=20)
    global iatempcs, iatemp1ms, iatemp2ms, iatempci, iatemp1mi, iatemp2mi, imcs, im1ms, im2ms, imci, im1mi, im2mi, irickcs, irick1ms, irick2ms, irickci, irick1mi, irick2mi
    iatempcs = StringVar()
    iatempcs.set("No Asignado")
    iatemp1ms = StringVar()
    iatemp1ms.set("No Asignado")
    iatemp2ms = StringVar()
    iatemp2ms.set("No Asignado")
    iatempci = StringVar()
    iatempci.set("No Asignado")
    iatemp1mi = StringVar()
    iatemp1mi.set("No Asignado")
    iatemp2mi = StringVar()
    iatemp2mi.set("No Asignado")
    imcs = StringVar()
    imcs.set("No Asignado")
    im1ms = StringVar()
    im1ms.set("No Asignado")
    im2ms = StringVar()
    im2ms.set("No Asignado")
    imci = StringVar()
    imci.set("No Asignado")
    im1mi = StringVar()
    im1mi.set("No Asignado")
    im2mi = StringVar()
    im2mi.set("No Asignado")
    irickcs = StringVar()
    irickcs.set("No Asignado")
    irick1ms = StringVar()
    irick1ms.set("No Asignado")
    irick2ms = StringVar()
    irick2ms.set("No Asignado")
    irickci = StringVar()
    irickci.set("No Asignado")
    irick1mi = StringVar()
    irick1mi.set("No Asignado")
    irick2mi = StringVar()
    irick2mi.set("No Asignado")
    def denticion(event):
        if dent.get() == "Temporaria":

            global iatemp,iatempcsL,iatempcsE,iatemp1msL,iatemp1msE,iatemp2msL,iatemp2msE,iatempciL,iatempciE,iatemp1miL,iatemp1miE,iatemp2miL,iatemp2miE
            global iatempcs,iatemp1ms,iatemp2ms,iatempci,iatemp1mi,iatemp2mi
            iatemp = ttk.Label(diagnostico_frame, text='A-Indice de Arcadas Temporarias')
            iatemp.grid(column=1, row=24, pady=10)

            iatempcs = StringVar()
            iatempcsL = ttk.Label(diagnostico_frame, text='Canino Superior')
            iatempcsL.grid(column=0, row=25)
            iatempcsE = ttk.Entry(diagnostico_frame, textvariable=iatempcs)
            iatempcsE.grid(column=0, row=26)

            iatemp1ms = StringVar()
            iatemp1msL = ttk.Label(diagnostico_frame, text='1° Molar Superior')
            iatemp1msL.grid(column=1, row=25)
            iatemp1msE = ttk.Entry(diagnostico_frame, textvariable=iatemp1ms)
            iatemp1msE.grid(column=1, row=26)

            iatemp2ms = StringVar()
            iatemp2msL = ttk.Label(diagnostico_frame, text='2° Molar Superior')
            iatemp2msL.grid(column=2, row=25)
            iatemp2msE = ttk.Entry(diagnostico_frame, textvariable=iatemp2ms)
            iatemp2msE.grid(column=2, row=26)

            iatempci = StringVar()
            iatempciL = ttk.Label(diagnostico_frame, text='Canino Inferior')
            iatempciL.grid(column=0, row=27)
            iatempciE = ttk.Entry(diagnostico_frame, textvariable=iatempci)
            iatempciE.grid(column=0, row=28)

            iatemp1mi = StringVar()
            iatemp1miL = ttk.Label(diagnostico_frame, text='1° Molar Inferior')
            iatemp1miL.grid(column=1, row=27)
            iatemp1miE = ttk.Entry(diagnostico_frame, textvariable=iatemp1mi)
            iatemp1miE.grid(column=1, row=28)

            iatemp2mi = StringVar()
            iatemp2miL = ttk.Label(diagnostico_frame, text='2° Molar Inferior')
            iatemp2miL.grid(column=2, row=27)
            iatemp2miE = ttk.Entry(diagnostico_frame, textvariable=iatemp2mi)
            iatemp2miE.grid(column=2, row=28)

        if dent.get() == "Mixta":

            global im,imcsL,imcsE, im1msL,im1msE,im2msL,im2msE, imciL,imciE,im1miL,im1miE,im2miL,im2miE,imcs, im1ms, im2ms, imci, im1mi, im2mi

            im = ttk.Label(diagnostico_frame, text='B-Indice Martinez')
            im.grid(column=1, row=24, pady=10)

            imcs = StringVar()
            imcsL = ttk.Label(diagnostico_frame, text='Canino Superior')
            imcsL.grid(column=0, row=25)
            imcsE = ttk.Entry(diagnostico_frame, textvariable=imcs)
            imcsE.grid(column=0, row=26)

            im1ms = StringVar()
            im1msL = ttk.Label(diagnostico_frame, text='1° Molar Superior')
            im1msL.grid(column=1, row=25)
            im1msE = ttk.Entry(diagnostico_frame, textvariable=im1ms)
            im1msE.grid(column=1, row=26)

            im2ms = StringVar()
            im2msL = ttk.Label(diagnostico_frame, text='2° Molar Superior')
            im2msL.grid(column=2, row=25)
            im2msE = ttk.Entry(diagnostico_frame, textvariable=im2ms)
            im2msE.grid(column=2, row=26)

            imci = StringVar()
            imciL = ttk.Label(diagnostico_frame, text='Canino Inferior')
            imciL.grid(column=0, row=27)
            imciE = ttk.Entry(diagnostico_frame, textvariable=imci)
            imciE.grid(column=0, row=28)

            im1mi = StringVar()
            im1miL = ttk.Label(diagnostico_frame, text='1° Molar Inferior')
            im1miL.grid(column=1, row=27)
            im1miE = ttk.Entry(diagnostico_frame, textvariable=im1mi)
            im1miE.grid(column=1, row=28)

            im2mi = StringVar()
            im2miL = ttk.Label(diagnostico_frame, text='2° Molar Inferior')
            im2miL.grid(column=2, row=27)
            im2miE = ttk.Entry(diagnostico_frame, textvariable=im2mi)
            im2miE.grid(column=2, row=28)
            
            global irick

            irick.grid_forget()
            iatemp.grid_forget()
            iatempcsL.grid_forget()
            iatempcsE.grid_forget()
            iatemp1msL.grid_forget()
            iatemp1msE.grid_forget()
            iatemp2msL.grid_forget()
            iatemp2msE.grid_forget()
            iatempciL.grid_forget()
            iatempciE.grid_forget()
            iatemp1miL.grid_forget()
            iatemp1miE.grid_forget()
            iatemp2miL.grid_forget()
            iatemp2miE.grid_forget()

        if dent.get() == "Permanente":

            global irickcs, irick1ms, irick2ms, irickci, irick1mi, irick2mi

            irick = ttk.Label(diagnostico_frame, text='C-Indice de Ricketts')
            irick.grid(column=1, row=24, pady=10)

            irickcs = StringVar()
            irickcsL = ttk.Label(diagnostico_frame, text='Canino Superior')
            irickcsL.grid(column=0, row=25)
            irickcsE = ttk.Entry(diagnostico_frame, textvariable=irickcs)
            irickcsE.grid(column=0, row=26)

            irick1ms = StringVar()
            irick1msL = ttk.Label(diagnostico_frame, text='1° Molar Superior')
            irick1msL.grid(column=1, row=25)
            irick1msE = ttk.Entry(diagnostico_frame, textvariable=irick1ms)
            irick1msE.grid(column=1, row=26)

            irick2ms = StringVar()
            irick2msL = ttk.Label(diagnostico_frame, text='2° Molar Superior')
            irick2msL.grid(column=2, row=25)
            irick2msE = ttk.Entry(diagnostico_frame, textvariable=irick2ms)
            irick2msE.grid(column=2, row=26)

            irickci = StringVar()
            irickciL = ttk.Label(diagnostico_frame, text='Canino Inferior')
            irickciL.grid(column=0, row=27)
            irickciE = ttk.Entry(diagnostico_frame, textvariable=irickci)
            irickciE.grid(column=0, row=28)

            irick1mi = StringVar()
            irick1miL = ttk.Label(diagnostico_frame, text='1° Molar Inferior')
            irick1miL.grid(column=1, row=27)
            irick1miE = ttk.Entry(diagnostico_frame, textvariable=irick1mi)
            irick1miE.grid(column=1, row=28)

            irick2mi = StringVar()
            irick2miL = ttk.Label(diagnostico_frame, text='2° Molar Inferior')
            irick2miL.grid(column=2, row=27)
            irick2miE = ttk.Entry(diagnostico_frame, textvariable=irick2mi)
            irick2miE.grid(column=2, row=28)

            im.grid_forget()
            imcsL.grid_forget()
            imcsE.grid_forget()
            im1msL.grid_forget()
            im1msE.grid_forget()
            im2msL.grid_forget()
            im2msE.grid_forget()
            imciL.grid_forget()
            imciE.grid_forget()
            im1miL.grid_forget()
            im1miE.grid_forget()
            im2miL.grid_forget()
            im2miE.grid_forget()

    global dent
    dent = StringVar()
    dentL = ttk.Label(diagnostico_frame, text='Denticion')
    dentL.grid(column=1, row=21)
    dentE = ttk.Combobox(diagnostico_frame, textvariable=dent , values=["Permanente", "Mixta", "Temporaria"])
    dentE.current(2)
    dentE.bind('<<ComboboxSelected>>', denticion)
    dentE.grid(column=1, row=22)

    tituloan = ttk.Label(diagnostico_frame, text='Analisis Transversal', font=14).grid(pady=5, column=1, row=23)

    titulov = ttk.Label(diagnostico_frame, text='Analisis Vertical', font=14).grid(pady=5, column=1, row=29)

    global profpaladar
    profpaladar = StringVar()
    profpaladarL = ttk.Label(diagnostico_frame, text='Prof. Paladar(.mm)')
    profpaladarL.grid(column=1, row=30)
    profpaladarE = ttk.Entry(diagnostico_frame, textvariable=profpaladar)
    profpaladarE.grid(column=1, row=31)

    titulodis = ttk.Label(diagnostico_frame, text='Analisis de Discrepancia', font=14).grid(pady=5, column=1, row=32)

    global discrepancia
    discrepancia = StringVar()
    discrepanciaL = ttk.Label(diagnostico_frame, text='Discrepancia Dentoalveolar')
    discrepanciaL.grid(column=1, row=33)
    discrepanciaE = ttk.Combobox(diagnostico_frame, textvariable=discrepancia, values=["Aumentada", "Disminuida", "Normal"])
    discrepanciaE.grid(column=1, row=34)

    titulocef = ttk.Label(diagnostico_frame, text="Diagnostico Cefalometrico", font=20).grid(pady=10, column=4, row= 20)
    titulpd = ttk.Label(diagnostico_frame, text="Problemas Dentarios" , font=1).grid(pady=5, column=4, row= 21)

    global rcanina, rmolar, anginter,convexidad, altfaci, protrusionl, pfacial, ejef, apman, amax, pmax

    trcanina = ttk.Label(diagnostico_frame, text="Relacion Canina").grid(pady=5, column=3, row=23)
    rcanina = StringVar()
    rcaninae = ttk.Entry(diagnostico_frame, textvariable=rcanina).grid(pady=5, column=3, row=24)
    trmolar = ttk.Label(diagnostico_frame, text="Relacion Molar").grid(pady=5, column=4, row= 23)
    rmolar = StringVar()
    rmolare = ttk.Entry(diagnostico_frame, textvariable=rmolar).grid(pady=5, column=4, row=24)
    tanginter = ttk.Label(diagnostico_frame, text="Angulo Interincisivo").grid(pady=5, column=5, row= 23)
    anginter = StringVar()
    angintere = ttk.Entry(diagnostico_frame, textvariable=anginter).grid(pady=5, column=5, row=24)

    titulpmm = ttk.Label(diagnostico_frame, text="Problemas Maxilomandibulares", font=1).grid(pady=5, column=4, row= 25)

    tconvexidad = ttk.Label(diagnostico_frame, text="Convexidad").grid(pady=5, column=3, row=26)
    convexidad = StringVar()
    convexidade = ttk.Entry(diagnostico_frame, textvariable=convexidad).grid(pady=5, column=3, row=27)
    taltfaci = ttk.Label(diagnostico_frame, text="Altura Facial Inferior").grid(pady=5, column=5, row= 26)
    altfaci = StringVar()
    altfacie = ttk.Entry(diagnostico_frame, textvariable=altfaci).grid(pady=5, column=5, row=27)

    titulpe = ttk.Label(diagnostico_frame, text="Problemas Esteticos", font=1).grid(pady=5, column=4, row= 28)

    tprotrusionl = ttk.Label(diagnostico_frame, text="Protrusion Labial").grid(pady=5, column=4, row=31)
    protrusionl = StringVar()
    protrusionle = ttk.Entry(diagnostico_frame, textvariable=protrusionl).grid(pady=5, column=4, row=32)

    titulpcf = ttk.Label(diagnostico_frame, text="Problemas Creneofaciales", font=1).grid(pady=5, column=4, row= 28)

    tpfacial = ttk.Label(diagnostico_frame, text="Profundidad Facial").grid(pady=5, column=3, row=29)
    pfacial = StringVar()
    pfaciale = ttk.Entry(diagnostico_frame, textvariable=pfacial).grid(pady=5, column=3, row=30)
    tejef = ttk.Label(diagnostico_frame, text="Eje Facial").grid(pady=5, column=4, row= 29)
    ejef = StringVar()
    ejefe = ttk.Entry(diagnostico_frame, textvariable=ejef).grid(pady=5, column=4, row=30)
    tapman = ttk.Label(diagnostico_frame, text="Ang. Plano Mandibular").grid(pady=5, column=5, row= 29)
    apman = StringVar()
    apmane = ttk.Entry(diagnostico_frame, textvariable=apman).grid(pady=5, column=5, row=30)
    tpmax = ttk.Label(diagnostico_frame, text="Profundidad Maxilar").grid(pady=5, column=5, row=31)
    pmax = StringVar()
    pmaxe = ttk.Entry(diagnostico_frame, textvariable=pmax).grid(pady=5, column=5, row=32)
    tamax = ttk.Label(diagnostico_frame, text="Altura Maxilar").grid(pady=5, column=3, row= 31)
    amax = StringVar()
    amaxe = ttk.Entry(diagnostico_frame, textvariable=amax).grid(pady=5, column=3, row=32)

    

    ttk.Button(diagnostico_frame, text="Guardar", command=guardar).grid(row=999,pady=4, column=3)
    ttk.Button(diagnostico_frame, text="Back", command=back_to_main).grid(row=999,column=4,pady=5)
    
    
def cargar_paciente():
    patient = carpeta+"/"+lista.get()+".json"
    abrir = open(patient)
    datos = json.load(abrir)


    #Datos Filiatorios
    global name
    name = datos['General']['Paciente']['Paciente']
    entry_base_input.delete(0, END)
    entry_base_input.insert(tk.INSERT, string=name)

    global sex
    sex = datos['General']['Paciente']['Sexo']
    sexoE.delete(0, END)
    sexoE.insert(tk.INSERT, string=sex)
    def sexo():
            if sex == "Femenino":
                global embarazo
                global embarazoE
                global embarazoL       
                embarazo = datos['General']['Paciente']['Embarazo']
                embarazoL = ttk.Label(datosfiliatorios_frame,text="Embarazo")
                embarazoL.grid(row=15, column=1,sticky=W, pady=5)

                embarazoE = ttk.Entry(datosfiliatorios_frame,textvariable="", width= 21)
                embarazoE.delete(0, END)
                embarazoE.configure(textvariable=embarazo)
                embarazoE.insert(tk.INSERT, string=embarazo)
                embarazo = StringVar()
                embarazo.set('')
                embarazoE.grid(row=16, column=1,sticky=N,pady=5, padx= 3)
            if sex == "Masculino":
                embarazoL.grid_forget()
                embarazoE.grid_forget()
    sexo()

    date_consulta = datos['General']['Paciente']['Fecha_Consulta']
    fechaE.delete(0, END)
    fechaE.insert(tk.INSERT, string=date_consulta)

    treatments = datos['General']['Paciente']['Tratamientos']
    tratamientosE.delete(0, END)
    tratamientosE.insert(tk.INSERT, string=treatments)

    birth = datos['General']['Paciente']['Fecha_Nacimiento']
    edadE.delete(0, END)
    edadE.insert(tk.INSERT, string=birth)

    address = datos['General']['Paciente']['Direccion']
    direccionE.delete(0, END)
    direccionE.insert(tk.INSERT, string=address)

    tel = datos['General']['Paciente']['Telefono']
    telefonoE.delete(0, END)
    telefonoE.insert(tk.INSERT, string=tel)

    obra = birth = datos['General']['Paciente']['Obra_Social']
    obrasocialE.delete(0, END)
    obrasocialE.insert(tk.INSERT, string=obra)

    consult = datos['General']['Paciente']['Motivo_de_Consulta']
    motivo_de_consultaE.delete(0, END)
    motivo_de_consultaE.insert(tk.INSERT, string=consult)
    
    #Enfermedades
    breath = datos['General']['Paciente']['Enf_Respiratorias']
    addEntrya.delete(0, END)
    addEntrya.insert(tk.INSERT, string=breath)
    hearth = datos['General']['Paciente']['Enf_Cardiacas']
    addEntryb.delete(0, END)
    addEntryb.insert(tk.INSERT, string=hearth)
    allergic = datos['General']['Paciente']['Enf_Alergicas']
    addEntryc.delete(0, END)
    addEntryc.insert(tk.INSERT, string=allergic)
    selfinmune = datos['General']['Paciente']['Enf_Autoinmunes']
    addEntryd.delete(0, END)
    addEntryd.insert(tk.INSERT, string=selfinmune)
    renal = breath = datos['General']['Paciente']['Enf_Renales']
    addEntrye.delete(0, END)
    addEntrye.insert(tk.INSERT, string=renal)
    surgery = datos['General']['Paciente']['Cirugias_Previas']
    addEntryf.delete(0, END)
    addEntryf.insert(tk.INSERT, string=surgery)
    paciente_health = breath, hearth, allergic, selfinmune, renal, surgery
    print(paciente_health)
    #Fotos
    osuperior = datos['General']['Paciente']['Fotos']['Oclusal_Superior'] 
    oinferior = datos['General']['Paciente']['Fotos']['Oclusal_Inferior']
    lizq = datos['General']['Paciente']['Fotos']['Lateral_Izquierda']   
    lder = datos['General']['Paciente']['Fotos']['Lateral_Derecha']
    front = datos['General']['Paciente']['Fotos']['Frente']
    face = datos['General']['Paciente']['Fotos']['Cara']
    pizq = datos['General']['Paciente']['Fotos']['Perfil_Izquierdo']
    pder = datos['General']['Paciente']['Fotos']['Perfil_Derecho']
    paciente_fotos = osuperior, oinferior, lizq, lder, front, face, pizq, pder
    print(paciente_fotos)
    #Diagnostico
    biotipo = datos['General']['Paciente']['Diagnostico']['Biotipo_Facial']
    habits = datos['General']['Paciente']['Diagnostico']['Habitos_Parafuncionales']
    positions = datos['General']['Paciente']['Diagnostico']['Malposiciones']
    aling = datos['General']['Paciente']['Diagnostico']['Alineacion_Interarcada']
    cross = datos['General']['Paciente']['Diagnostico']['Entrecruzamiento']
    mediallf = datos['General']['Paciente']['Diagnostico']['Linea_Media_Facial']
    medialld = datos['General']['Paciente']['Diagnostico']['Linea_Media_Dentaria']
    overbite = datos['General']['Paciente']['Diagnostico']['Overbite']
    overjetd = datos['General']['Paciente']['Diagnostico']['Overjet']
    spee = datos['General']['Paciente']['Diagnostico']['Curva_Spee']
    cmi = datos['General']['Paciente']['Diagnostico']['Clase_Molar_Izquierda']
    cmd = datos['General']['Paciente']['Diagnostico']['Clase_Molar_Derecha']
    cci = datos['General']['Paciente']['Diagnostico']['Clase_Canina_Izquierda']
    ccd = datos['General']['Paciente']['Diagnostico']['Clase_Canina_Derecha']
    denticion = datos['General']['Paciente']['Diagnostico']['Denticion']
    iarctemcs = datos['General']['Paciente']['Diagnostico']['I_arctemp_Cs']
    iarctem1ms = datos['General']['Paciente']['Diagnostico']['I_arctemp_1ms']
    iarctem2ms = datos['General']['Paciente']['Diagnostico']['I_arctemp_2ms']
    iarctemci = datos['General']['Paciente']['Diagnostico']['I_arctemp_Ci']
    iarctem1mi = datos['General']['Paciente']['Diagnostico']['I_arctemp_1mi']
    iarctem2mi = datos['General']['Paciente']['Diagnostico']['I_arctemp_2mi']
    imcs = datos['General']['Paciente']['Diagnostico']['I_m_Cs']
    im1ms = datos['General']['Paciente']['Diagnostico']['I_m_1ms']
    im2ms = datos['General']['Paciente']['Diagnostico']['I_m_2ms']
    imci = datos['General']['Paciente']['Diagnostico']['I_m_Ci']
    im1mi = datos['General']['Paciente']['Diagnostico']['I_m_1mi']
    im2mi = datos['General']['Paciente']['Diagnostico']['I_m_2mi']
    irickcs = datos['General']['Paciente']['Diagnostico']['I_rick_Cs']
    irick1ms = datos['General']['Paciente']['Diagnostico']['I_rick_1ms']
    irick2ms = datos['General']['Paciente']['Diagnostico']['I_rick_2ms']
    irickci = datos['General']['Paciente']['Diagnostico']['I_rick_Ci']
    irick1mi = datos['General']['Paciente']['Diagnostico']['I_rick_1mi']
    irick2mi = datos['General']['Paciente']['Diagnostico']['I_rick_2mi']
    profundidadp = datos['General']['Paciente']['Diagnostico']['Prof_Paladar']
    relac = datos['General']['Paciente']['Diagnostico']['Relacion_canina']
    relam = datos['General']['Paciente']['Diagnostico']['Relacion_molar']
    angulointer = datos['General']['Paciente']['Diagnostico']['Angulo_Interincisivo']
    convex = datos['General']['Paciente']['Diagnostico']['Convexidad']
    alturafac = datos['General']['Paciente']['Diagnostico']['Altura_facial']
    protlab = datos['General']['Paciente']['Diagnostico']['Protrusion_labial']
    profundidadf = datos['General']['Paciente']['Diagnostico']['Profundidad_facial']
    ejefacial = datos['General']['Paciente']['Diagnostico']['Eje_facial']
    angplanmand = datos['General']['Paciente']['Diagnostico']['Ang_Plano_mandibular']
    altmax = datos['General']['Paciente']['Diagnostico']['Altura_maxilar']
    profundidadm = datos['General']['Paciente']['Diagnostico']['Profundidad_maxilar']
    abrir.close    

def pagina_inicial():
        global lista, carpeta
        carpeta = r'C:\Users\diego\Desktop\ProgrmacionPhyton\consultorio\pacientes\grupopacientes'
        files = [os.path.splitext(filename)[0] for filename in os.listdir(carpeta)]
        lista = ttk.Combobox(inicio, textvariable=files , values=files)
        lista.pack(fill='x')
        lista.grid(row=1)
        cargar = ttk.Button(inicio, text="Cargar Paciente", command=cargar_paciente)
        cargar.grid(row=1,column=1)
        
        
        ttk.Label(inicio, text="Bienvenidos a Dentalis-Ingreso de Pacientes").grid(row=0,pady=5)
        ttk.Button(inicio, text="1-Datos Filiatorios", command=show_datos_filiatorios).grid(row=2,pady=5)
        ttk.Button(inicio, text="2-Antecedentes Patologicos", command=show_antecedentes_patologicos).grid(row=4,pady=5)
        ttk.Button(inicio, text="3-Motivo de Consulta", command=show_motivo_consulta).grid(row=6,pady=5)
        ttk.Button(inicio, text="4-Odontograma", command=show_odontograma).grid(row=8,pady=5)
        ttk.Button(inicio, text="5-Agregar Fotos", command=show_fotos).grid(row=10,pady=5)
        ttk.Button(inicio, text="6-Diagnostico", command=show_diagnostico).grid(row=12,pady=5)
        ttk.Button(inicio, text="Guardar", command=guardar).grid(row=14,pady=5)
        

 
root = tk.Tk()
inicio = ttk.Frame(root)
root.title("Dentalist")
root.geometry('1600x900')
root.resizable(True, True)
root.iconbitmap(r'C:\Users\diego\Desktop\ProgrmacionPhyton\consultorio\pacientes\image/den.ico')
inicio.pack()

datosfiliatorios_frame = ttk.Frame(root)
antecedentes_patologicos_frame = ttk.Frame(root)
odontograma_frame = ttk.Frame(root)
motivoconsulta_frame = ttk.Frame(root)
fotos_frame = ttk.Frame(root)
diagnostico_frame = ttk.Frame(root)
current_frame = inicio

pagina_inicial()
create_datos_filiatorios()
create_motivo_consulta()
create_antecedentes_patologicos()
create_odontograma()
create_fotos()
create_diagnostico()

root.mainloop()

