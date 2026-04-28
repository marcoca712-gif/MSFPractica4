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

import control as ctrl
import numpy as np
import matplotlib.pyplot as plt


t0, tend, dt, w, h = 0, 15, 1e-3, 10, 5
N = round((tend - t0) / dt) + 1
t = np.linspace(t0, tend, N)


u = np.zeros_like(t)
u[t >= 1] = 1.0

def endocrino_tf(R1, R2, L, C):
    num = [L, R2]
    den = [C * L * R1, (C * R1 * R2) + L, R1 + R2]
    sys = ctrl.tf(num, den)
    return sys

# 1. Respuesta hormonal basal (Control)
R1_s, R2_s, L_s, C_s = 1e3, 100e3, 100e-3, 1e-6
sys_control = endocrino_tf(R1_s, R2_s, L_s, C_s)

# 2. Respuesta hormonal alterada (Caso)
R1_c, R2_c, L_c, C_c = 1e3, 1000, 100e-3, 1000e-6
sys_caso = endocrino_tf(R1_c, R2_c, L_c, C_c)

# Respuestas en Lazo Abierto
x0 = 0
_, Vs_control = ctrl.forced_response(sys_control, t, u, x0)
_, Vs_caso = ctrl.forced_response(sys_caso, t, u, x0)

# Controlador PID
def controlador(kP, kI, kD, sys):
    Cr = 1e-6
    Re = 1 / (kI * Cr)
    Rr = kP * Re
    Ce = kD / Rr
    numPID = [Re * Rr * Ce * Cr, (Re * Ce + Rr * Cr), 1]
    denPID = [Re * Cr, 0]
    PID = ctrl.tf(numPID, denPID)
    X = ctrl.series(PID, sys)
    sysPID = ctrl.feedback(X, 1, sign=-1)
    return sysPID

casoPID = controlador(55.0, 150.0, 0.05, sys_caso)

# Respuesta en lazo cerrado tomando el control como referencia
_, PID_res = ctrl.forced_response(casoPID, t, Vs_control, x0)

# --- Generación de Gráfica Única (Subplot b) ---
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(t, Vs_control, '-', linewidth=1.5, color=[0.1, 0.5, 0.1], label=r'$V_s(t)$: Control')
ax.plot(t, Vs_caso, '-', linewidth=1.5, color=[0.7, 0.1, 0.1], label=r'$V_s(t)$: Caso')
ax.plot(t, PID_res, ':', linewidth=2, color=[0.2, 0.4, 0.8], label=r'$PID(t)$')


ax.set_xlabel(r'$t$ [s]')
ax.set_ylabel(r'$V(t)$ [V]')
ax.set_xlim(0, 15)
ax.set_ylim(-0.2, 1.4)
ax.grid(False)
ax.legend(loc='lower center', bbox_to_anchor=(0.5, 1.02), ncol=3, frameon=False, fontsize=11)
ax.text(0.01, 1.05, '(b)', transform=ax.transAxes, fontweight='bold')

plt.tight_layout()
plt.show()

# Guardar figura
fig.savefig('Sistema_Endocrino_Regulacion_PID.pdf')


