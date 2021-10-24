def massa(l, t, m):
    porc_perna = 4.4*(1-t/l)/100
    porc_pe = 1.5/100
    porc_perdida = porc_pe + porc_perna
    porc_pessoa = 1 - porc_perdida
    m_pe = m * porc_pe/porc_pessoa
    m_perna = m * porc_perna/porc_pessoa
    return m_perna, m_pe



def momento_inercia(l,t,leg,n,m):
    l = float(l)/100
    t = float(t)/100
    leg = float(leg)/100
    n = float(n)
    m = float(m)
    n_pe = {
            32:(22.1+22.5)/2,
            33:(22.6+23)/2,
            34:(23.1+23.5)/2,
            35:(23.6+24)/2,
            36:(24.1+24.5)/2,
            37:(24.6+25)/2,
            38:(25.1+25.5)/2,
            39:(25.6+26)/2,
            40:(26.1+26.5)/2,
            41:(26.6+27)/2,
            42:(27.1+27.5)/2
            }   

    comp = n_pe[n]
    larg = comp/3
    r = (larg*2/3)/2
    m_perna, m_pe = massa(l,t,m)

    mi_perna = m_perna*(r**2/4+l**2/3)
    mi_pe = m_pe*(comp**2+(leg - l)**2)/2 + m_pe*(l**2+(comp/2)**2)  

    mi_protese = mi_perna + mi_perna
    return mi_protese

"""
l = float(input("Digite a medida do joelho até o tornozelo (em cm): "))/100
t = float(input("Digite a medida do joelho até o final do coto (em cm): "))/100
leg = float(input("Digite a medida do joelho até a sola do pé (em cm): "))
n = int(input("Digite o número do sapato: "))
m = float(input("Digite a massa da pessoa (em kg): "))

print("O momento de inércia da prótese equivale a %.2f kg.m²" %momento_inercia(l,t,leg,n,m))"""

