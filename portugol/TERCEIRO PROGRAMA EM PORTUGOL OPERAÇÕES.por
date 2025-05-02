/*TERCEIRO PROGRAMA - OPERAÇÕES */

programa {
  funcao inicio() {
    inteiro n1, n2
    real soma, sub, mult, div
    escreva("Digite o Primeiro numero: ")
    leia(n1)
    escreva("Digite o Segundo número: ")
    leia(n2)
    soma = n1 + n2
    sub = n1 - n2
    mult = n1 * n2
    div = n1 / n2
    escreva("O resultado é Soma: ", soma,"  Sub: ",sub, " Mult: ", mult, " Div: ",div)
  }
}
