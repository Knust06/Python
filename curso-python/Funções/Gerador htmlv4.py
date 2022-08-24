def tag_bloco(conteudo,*args, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_lista(*itens):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco')) #<div class="success">bloco</div>
    print(tag_bloco('inline e classe', 'info', True)) #<span class="info">inline e classe</span>
    print(tag_bloco('inline', inline=True)) #<span class="success">inline</span>
    print(tag_bloco(inline=True, conteudo='inline')) #<span class="success">inline</span>
    print(tag_bloco('falhou', classe='error')) #<div class="error">falhou</div>
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info')) #<div class="info"><ul><li>Item 1</li><li>Item 2</li></ul></div>
    print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe = 'info', inline=True))
    #print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe = 'info', True)) sem o inline= True ele da um erro de sintaxa pois o argumento segue um argumento nomeado

    
