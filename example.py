meu_dicionario = {
    "ola":"mundo",
    "estou":"aprendendo"
}

outro_dicionario = {
    **meu_dicionario,
    "id": "me_id"
}


print(outro_dicionario)