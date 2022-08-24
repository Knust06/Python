def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


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
    
