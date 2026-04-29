"""
Práctica 4: Sistema Endocrino

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Marco Antonio Campoy Alegria
Número de control: 21212145
Correo institucional: L21212145@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""

# Librerías
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Datos de la simulación
x0, t0, tend, dt, w, h = 0, 0, 10, 1E-3, 7, 3.5
N = int(tend/dt) + 1
t = np.linspace(t0, tend, N)
u2 = np.zeros(N); u2[round(1/dt):] = 1  # Step

# Parámetros del circuito
R1 = 1e3
L  = 3.3e-3
R2 = 1e3
C  = 100e-6

# Función de transferencia
Num = [1e3]
Den = [(1000e-6*3.3e-3*1e3), (1000e-6*1e3*1e3 + 3.3e-3), (1e3 + 1e3)]
sys_ctrl = ctrl.tf(Num, Den)
sys_caso = ctrl.tf(Num, Den)
print(f"FT Control: {sys_ctrl}\n")
print(f"FT Caso:    {sys_caso}\n")

# Controlador PID
def controlador(kP, kI, kD, sys):
    Cr = 1e-6
    Re = 1 / (kI * Cr)
    Rr = kP * Re
    Ce = kD / Rr

    print(f"El valor de capacitancia Cr es de {Cr} Faradios.\n")
    print(f"El valor de resistencia Re es de {Re} Ohms.\n")
    print(f"El valor de resistencia Rr es de {Rr} Ohms.\n")
    print(f"El valor de capacitancia Ce es de {Ce} Faradios.\n")

    numPID = [Re*Rr*Ce*Cr, (Re*Ce + Rr*Cr), 1]
    denPID = [Re*Cr, 0]
    PID = ctrl.tf(numPID, denPID)
    print(f"FT Controlador PID: {PID}\n")

    X      = ctrl.series(PID, sys)
    sysPID = ctrl.feedback(X, 1, sign=-1)
    return sysPID

kP = 139.0244
kI = 3579.0025
kD = 0.182
sys_caso_LC = controlador(kP, kI, kD, sys_caso)
print(f"FT Caso LC: {sys_caso_LC}\n")

# Respuestas
_, F_ctrl   = ctrl.forced_response(sys_ctrl,    t, u2, x0)
_, F_caso   = ctrl.forced_response(sys_caso,    t, u2, x0)
_, PID_caso = ctrl.forced_response(sys_caso_LC, t, u2, x0)

# Colores
clr1 = [0.25, 0.51, 0.47]  # verde
clr2 = [0.50, 0.10, 0.05]  # rojo
clr3 = [0.00, 0.25, 0.40]  # azul

# Gráfica: Scope de Caso
fig, ax = plt.subplots(1, 1, figsize=(w, h))
fig.patch.set_facecolor('white')
ax.plot(t, u2,       '-', color=clr1, linewidth=1.5, label=r'$V_s(t):\ Control$')
ax.plot(t, F_caso,   '-', color=clr2, linewidth=1.0, label=r'$V_s(t):\ Caso$')
ax.plot(t, PID_caso, ':', color=clr3, linewidth=2.0, label=r'$PID$')
ax.set_xlim(0, 10); ax.set_xticks(np.arange(0, 11, 1))
ax.set_ylim(0, 1.2); ax.set_yticks(np.arange(0, 1.4, 0.2))
ax.set_xlabel(r'$t\ [s]$', fontsize=11)
ax.set_ylabel(r'$V_s(t)\ [V]$', fontsize=11)
ax.set_title('Scope de Caso', fontsize=10, fontweight='bold')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=3,
          fontsize=9, frameon=False)
plt.tight_layout()
plt.savefig('endocrino.pdf', bbox_inches='tight')
plt.show()