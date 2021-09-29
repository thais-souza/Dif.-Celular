#========================================================================================
# GERAÇÃO DE GRÁFICO PARA A SOLUÇÃO DADA POR AUDDYA
#========================================================================================
# DECLARAÇÃO DE MÓDULOS
#========================================================================================
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#========================================================================================
# VARIÁVEIS GLOBAIS
#========================================================================================
R = 1.5          # TAMANHO DO RAIO DA CIRCUNFERÊNCIA
SIGMA = R / 10   # CONSTANTE
NI = 0.002
MI = 0.129
T = -0.1
#========================================================================================
# DETERMINAÇÃO DOS DESLOCAMENTOS
#========================================================================================
r = np.linspace ( 0.05 , 1.5 , 30 )
t = np.radians ( np.linspace ( 0, 360, 20 ) )
rc , tc = np.meshgrid ( r , t )
u_r = ( ( ( np.exp ( ( r - R ) / SIGMA ) * ( NI/MI) * 1.5 * SIGMA )    # DESLOCAMENTO INTRACELULAR
          + r ) / 6.0 ) * ( - T / ( NI + MI ) )
w_r = ( ( ( - np.exp ( ( r - R ) / SIGMA ) * 1.5 * SIGMA )  # DESLOCAMENTO EXTRACELULAR
          + r ) / 6.0 ) * ( - T / ( NI + MI ) )
diferenca =  u_r - w_r
#========================================================================================
# DETERMINAÇÃO DAS DEFORMAÇÕES
#========================================================================================
e_irr = ( ( 1.0 + 1.5 * (NI/MI) *  np.exp ( ( r - R ) / SIGMA ) ) / 6.0 ) * ( - T / ( NI + MI ) )
e_irr_g = abs( ( ( 1.0 + 1.5 * (NI/MI) * np.exp ( ( rc - R ) / SIGMA ) ) / 6.0 ) *  ( - T / ( NI + MI ) ) )
e_itt = u_r / r
e_itt_g = abs(u_r / rc)
e_err = ( ( 1.0 - 1.5 * np.exp ( ( r - R ) / SIGMA ) ) / 6.0 ) * ( - T / ( NI + MI ) )
e_err_g = abs( ( ( 1.0 - 1.5 * np.exp ( ( rc - R ) / SIGMA ) ) / 6.0 ) * ( - T / ( NI + MI ) ))
e_ett = w_r / r
e_ett_g = abs( w_r / rc )
#========================================================================================
# DETERMINAÇÃO DAS TENSÕES
#========================================================================================
p = - 2 * NI * ( e_irr + e_itt )
q = - 2 * MI * ( e_ett + e_err )
t_irr = - p + 2 * NI * e_irr + T
t_itt = - p + 2 * NI * e_itt + T
t_err = - q + 2 * MI * e_err
t_ett = - q + 2 * MI * e_ett

#========================================================================================
# GERAÇÃO DOS GRÁFICOS
#========================================================================================
plt.rcParams.update({'font.size': 13})
plt.rcParams.update({'axes.titlepad':13})
#========================================================================================
# FIGURA 1
#========================================================================================
fig = plt.figure ()
#========================================================================================
# FIGURA 1 - GRÁFICO DOS DESLOCAMENTOS INTRA E EXTRACELULARES
#========================================================================================
desloc = fig.add_subplot ( 131 )
desloc.plot ( r , u_r , c = 'b' , linewidth = 0.5, linestyle = '--', label = "$U_r$" )
desloc.plot ( r , w_r , c = 'r' , lw = 0.5, ls = '-' , label = "$W_r$" )
desloc.plot ( r , diferenca , c = 'g', lw = 1.5, ls = 'dotted' , label = "$U_r - W_r$")
desloc.legend ( loc = "upper left" )
desloc.set_title ("Deslocamentos intra e extracelulares")
desloc.set_xlabel ( "r (mm)" )
desloc.set_ylabel ( "(mm)" )
#========================================================================================
# FIGURA 1 - GRÁFICO DAS DEFORMAÇÕES INTRA E EXTRACELULARES
#========================================================================================
defor = fig.add_subplot ( 132 )
defor.plot ( r , e_irr , c = 'b' , linewidth = 0.5, linestyle = '-',
             label = "$\epsilon^i_{rr}$" )
defor.plot ( r , e_itt , c = 'b' , lw = 0.5, ls = '--' ,
             label = r"$\epsilon^i_{\theta\theta}$" )
defor.plot ( r , e_err , c = 'r', lw = 1.5, ls = '-' ,
             label =  "$\epsilon^i_{rr}$" )
defor.plot ( r , e_ett , c = 'r', lw = 1.5, ls = '--' ,
             label = r"$\epsilon^e_{\theta\theta}$" )
defor.legend ( loc = "upper left" )
defor.set_title ("Deformações intra e extracelulares")
defor.set_xlabel ( "r (mm)" )
defor.set_ylabel ( "Deformações" )
#========================================================================================
# FIGURA 1 - GRÁFICO DAS TENSÕES INTRA E EXTRACELULARES
#========================================================================================
tensao = fig.add_subplot ( 133 )
tensao.plot ( r , t_irr , c = 'b' , linewidth = 0.5, linestyle = '-',
             label = r"$\tau^i_{rr}$" )
tensao.plot ( r , t_itt , c = 'b' , lw = 0.5, ls = '--' ,
             label = r"$\tau^i_{\theta\theta}$" )
tensao.plot ( r , t_err , c = 'r', lw = 1.5, ls = '-' ,
             label = r"$\tau^e_{rr}$" )
tensao.plot ( r , t_ett , c = 'r', lw = 1.5, ls = '--' ,
             label = r"$\tau^e_{\theta\theta}$" )
tensao.legend ( loc = "upper left" )
tensao.set_title ("Tensões intra e extracelulares")
tensao.set_xlabel ( "r (mm)" )
tensao.set_ylabel ( "Tensões ($N/mm^2$)" )
fig.subplots_adjust ( hspace = 0.1, wspace = 0.4)
#========================================================================================
# FIGURA 2
#========================================================================================
fig2 = plt.figure ()
#========================================================================================
# FIGURA 2 - GRÁFICO DA DEFORMAÇÃO INTRACELULAR (rr)
#========================================================================================
deforirr = fig2.add_subplot ( 221, projection = "polar" )
im3 = deforirr.contourf ( tc, rc, e_irr_g , cmap = "Blues" )
fig2.colorbar ( im3, pad=0.15,  label = " ")
deforirr.set_title ("Deformação $\epsilon^i_{rr}$ em módulo")
deforirr.set_xlabel ("r (mm)")
deforirr.tick_params(axis='y', which='major', labelsize=6)
#========================================================================================
# FIGURA 2 - GRÁFICO DA DEFORMAÇÃO INTRACELULAR (θθ)
#========================================================================================
deforitt = fig2.add_subplot ( 222, projection = "polar" )
im4 = deforitt.contourf ( tc, rc, e_itt_g , cmap = "Blues" )
fig2.colorbar ( im4 , pad=0.15)
deforitt.set_title ("Deformação $\epsilon^i_{θθ}$ em módulo")
deforitt.set_xlabel ("r (mm)")
deforitt.tick_params(axis='y', which='major', labelsize=6)
#========================================================================================
# FIGURA 2 - GRÁFICO DA DEFORMAÇÃO EXTRACELULAR (rr)
#========================================================================================
deforerr = fig2.add_subplot ( 223, projection = "polar" )
im5 = deforerr.contourf ( tc, rc, e_err_g, cmap = "Blues" )
fig2.colorbar ( im5 , pad=0.15)
deforerr.set_title ("Deformação $\epsilon^e_{rr}$ em módulo")
deforerr.set_xlabel ("r (mm)")
deforerr.tick_params(axis='y', which='major', labelsize=6)
#========================================================================================
# FIGURA 2 - GRÁFICO DA DEFORMAÇÃO EXTRACELULAR (θθ)
#========================================================================================
deforett = fig2.add_subplot ( 224, projection = "polar" )
im6 = deforett.contourf ( tc, rc, e_ett_g , cmap = "Blues" )
fig2.colorbar ( im6, pad=0.15)
deforett.set_title ("Deformação $\epsilon^e_{θθ}$ em módulo")
deforett.set_xlabel ("r (mm)")
deforett.tick_params(axis='y', which='major', labelsize=6)
#========================================================================================
# AJUSTE DO POSICIONAMENTO DOS GRÁFICOS NA FIGURA 2
#========================================================================================
fig2.subplots_adjust ( bottom = 0.1, left = 0.1, right = 0.9, top = 0.9, hspace = 0.7, wspace = 0.2)
#========================================================================================
# APRESENTAÇÃO DAS FIGURAS E GRÁFICOS
#========================================================================================
plt.show ()
