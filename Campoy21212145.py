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

# Librerias para calculo numerico y generacion de graficas
import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

# Configuración de tiempo y señal de entrada (Escalón unitario)
t0, tend, dt, w, h = 0, 15, 1e-3, 10, 5
N = round((tend - t0) / dt) + 1
t = np.linspace(t0, tend, N)

# Generación de estímulo glandular (Entrada Ve(t) de 1V en t=1s)
u = np.zeros_like(t)
u[t >= 1] = 1.0

def endocrino_tf(R1, R2, L, C):
    """
    Modelo de segundo orden para el sistema endocrino.
    H(s) = (Ls + R2) / (R1CLs^2 + (R1CR2 + L)s + (R1 + R2))
    """
    num = [L, R2]
    den = [C * L * R1, (C * R1 * R2) + L, R1 + R2]
    sys = ctrl.tf(num, den)
    return sys

# --- Definición de Sistemas (Control vs Caso) ---

# 1. Respuesta hormonal basal (Control)
# Valores que representan estabilidad y rapidez
R1_s, R2_s, L_s, C_s = 1e3, 100e3, 100e-3, 1e-6
sys_control = endocrino_tf(R1_s, R2_s, L_s, C_s)
print(f'FT Control (Estable): {sys_control}')

# 2. Respuesta hormonal alterada (Caso)
# Valores con mayor retardo y menor precisión
R1_c, R2_c, L_c, C_c = 1e3, 1000, 100e-3, 1000e-6
sys_caso = endocrino_tf(R1_c, R2_c, L_c, C_c)
print(f'FT Caso (Alterado): {sys_caso}')

# --- Respuestas en Lazo Abierto ---
x0 = 0
_, Vs_control = ctrl.forced_response(sys_control, t, u, x0)
_, Vs_caso = ctrl.forced_response(sys_caso, t, u, x0)

# --- Controlador PID para regulación hormonal ---
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

# Aplicación del PID al sistema alterado para recuperar la homeostasis
# Sintonización basada en el bloque PID del Simulink
casoPID = controlador(55.0, 150.0, 0.05, sys_caso)
print(f'FT Caso en lazo cerrado (PID): {casoPID}')

# Respuesta en lazo cerrado tomando el control como referencia
_, PID_res = ctrl.forced_response(casoPID, t, Vs_control, x0)

# --- Generación de Gráficas ---
fig, ax = plt.subplots(2, 1, sharex=True)

# Subplot (a): Estímulo vs Respuesta Basal
ax[0].plot(t, u, '--', linewidth=1, color='cyan', label=r'$V_e(t)$: Estímulo')
ax[0].plot(t, Vs_control, '-', linewidth=1.5, color=[0.1, 0.5, 0.1], label=r'$V_s(t)$: Control')
ax[0].set_title('Estímulo Glandular vs Respuesta Hormonal (Control)')
ax[0].set_ylabel(r'$V(t)$ [V]')
ax[0].set_xlim(0, 15)
ax[0].set_ylim(-0.2, 1.4)
ax[0].grid(False)
ax[0].legend(loc='lower center', bbox_to_anchor=(0.5, 1.12), ncol=2, frameon=False, fontsize=11)
ax[0].text(0.01, 1.05, '(a)', transform=ax[0].transAxes, fontweight='bold')

# Subplot (b): Control vs Caso Alterado vs Regulación PID
ax[1].plot(t, Vs_control, '-', linewidth=1.5, color=[0.1, 0.5, 0.1], label=r'$V_s(t)$: Control')
ax[1].plot(t, Vs_caso, '-', linewidth=1.5, color=[0.7, 0.1, 0.1], label=r'$V_s(t)$: Caso')
ax[1].plot(t, PID_res, ':', linewidth=2, color=[0.2, 0.4, 0.8], label=r'$PID(t)$: Regulación')

ax[1].set_title('Regulación Hormonal: Control vs Alteración vs PID')
ax[1].set_xlabel(r'$t$ [s]')
ax[1].set_ylabel(r'$V(t)$ [V]')
ax[1].set_xlim(0, 15)
ax[1].set_ylim(-0.2, 1.4)
ax[1].grid(False)
ax[1].legend(loc='lower center', bbox_to_anchor=(0.5, 1.12), ncol=3, frameon=False, fontsize=11)
ax[1].text(0.01, 1.05, '(b)', transform=ax[1].transAxes, fontweight='bold')

# Ajustes de formato
fig.set_size_inches(w, 2 * h)
fig.tight_layout(rect=[0, 0, 1, 0.95])

plt.show()

# Guardar figura
fig.savefig('Sistema_Endocrino_Regulacion_PID.pdf')