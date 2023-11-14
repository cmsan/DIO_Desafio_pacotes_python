num0=  ['# # #', '#   #', '#   #', '#   #', '# # #']#matriz que compõe o algarismo zero.
num1 = ['    #', '    #', '    #', '    #', '    #']#matriz que compõe o algarismo um.
num2 = ['# # #', '    #', '# # #', '#    ', '# # #']##matriz que compõe o algarismo dois.
num3 = ['# # #', '    #', '# # #', '    #', '# # #']#matriz que compõe o algarismo três.
num4 = ['#   #', '#   #', '# # #', '    #', '    #']#matriz que compõe o algarismo quatro.
num5 = ['# # #', '#    ', '# # #', '    #', '# # #']#matriz que compõe o algarismo cinco.
num6 = ['# # #', '#    ', '# # #', '#   #', '# # #']#matriz que compõe o nalgarismo seis.
num7 = ['# # #', '    #', '    #', '    #', '    #']#matriz que compõe o algarismo sete.
num8 = ['# # #', '#   #', '# # #', '#   #', '# # #']#matriz que compõe o algarismo oito.
num9 = ['# # #', '#   #', '# # #', '    #', '    #']#matriz que compõe o algarismo nove.

nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]#matriz com todos os algarismos.

inp = list(elem)#a variavel 'elem' não pode ser string, tem que ser uma lista(array).

def display():#Função que compõe o display que terá cinco linhas onde os algarismos serão exibidos.
    separator = '   '#O espaço entre cada algarisno.
    line0 = ''#linha 1 do display vazia.
    line1 = ''#linha 2 do display vazia.
    line2 = ''#linha 3 do display vazia.
    line3 = ''#linha 4 do display vazia.
    line4 = ''#linha 5 do display vazia.

    for i in inp:

        line0 += nums[int(i)][0]+separator
        line1 += nums[int(i)][1]+separator
        line2 += nums[int(i)][2]+separator
        line3 += nums[int(i)][3]+separator
        line4 += nums[int(i)][4]+separator

    print()
    print(line0)
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print()

display()
