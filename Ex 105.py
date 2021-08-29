def notas(*nota,sit=False):
    """
    Função analisar notas e situaçoes de alunos.
    :param nota:Cada nota do aluno
    :param sit:Opcional,Situação da média das notas.
    :return:Dicionario com varias informações.
    """
    r = dict()
    r['total']=len(nota)
    r['maior']=max(nota)
    r['menor']=min(nota)
    r['media']=sum(nota)/len(nota)
    if sit:
        if r['media']>7:
            r['situação']='BOA'
        elif r['media']>=5:
            r['situação']='RAZOÁVEL'
        else:
            r['situação']='RUIM'
    return r
resp = notas(6.5,4.3,7.6,sit=True)
print(resp)