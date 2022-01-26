#Projekt wymaga PySimpleGUI
import PySimpleGUI as sg
sg.theme('DarkGray13')
def calc(i,k,z):
    i=int(i)
    k=int(k)
    z=int(z)
    i=i*1000
    kk = k / i
    wynik = z / kk
    return wynik

layout= [[sg.Text('Kalkulator Koronawirusowy ')],
         [sg.InputText(size=(10)), sg.Text('Na ile tysięcy?')],
         [sg.InputText(size=(10)), sg.Text('Na ile ludzi?')],
         [sg.InputText(size=(10)), sg.Text('Ile?')],
         [sg.Button('Oblicz'), sg.Input("Tutaj pojawi się wynik",key='wynik')]]
window = sg.Window('Kalkulator Koronawirusowy', layout, size=(230, 150))
while True:
    event, values = window.read()
    if event == 'Oblicz':
        input_text = values['wynik']
        window['wynik'].update(calc(values[0],values[1],values[2]))
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break