def base64_encode(input_string):
    # Tabela de caracteres Base64
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    # Codifica a string de entrada em uma sequência de bytes
    input_bytes = input_string.encode('utf-8')

    # Inicializa a string codificada
    encoded_string = ""

    # Itera sobre os bytes de entrada em grupos de 3
    for i in range(0, len(input_bytes), 3):
        # Obtém os três bytes atuais
        chunk = input_bytes[i:i+3]

        # Obtém os valores dos bytes e adiciona zeros à esquerda se necessário
        chunk_values = [chunk[j] if j < len(chunk) else 0 for j in range(3)]
        
        # Obtém os índices dos caracteres correspondentes na tabela Base64
        indices = [(chunk_values[0] >> 2) & 0b111111, ((chunk_values[0] & 0b11) << 4) | ((chunk_values[1] >> 4) & 0b1111), ((chunk_values[1] & 0b1111) << 2) | ((chunk_values[2] >> 6) & 0b11), chunk_values[2] & 0b111111]

        # Adiciona os caracteres codificados à string codificada
        for index in indices:
            encoded_string += base64_chars[index]

    # Adiciona os caracteres de padding '=' conforme necessário
    padding = len(input_bytes) % 3
    if padding == 1:
        encoded_string += "=="
    elif padding == 2:
        encoded_string += "="

    return encoded_string

def base64_decode(encoded_string):
    # Tabela de caracteres Base64
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    # Inicializa a string decodificada
    decoded_string = ""

    # Remove os caracteres de padding '=' da string codificada
    encoded_string = encoded_string.rstrip('=')

    # Inicializa um contador de bits para rastrear a posição atual
    bit_counter = 0
    # Inicializa um buffer para armazenar os bits temporariamente
    buffer = 0
    # Itera sobre os caracteres codificados
    for char in encoded_string:
        # Calcula o valor do índice do caractere na tabela Base64
        char_value = base64_chars.index(char)
        # Adiciona o valor ao buffer na posição adequada
        buffer = (buffer << 6) | char_value
        # Atualiza o contador de bits
        bit_counter += 6
        # Se temos pelo menos 8 bits no buffer, podemos formar um byte decodificado
        while bit_counter >= 8:
            # Adiciona o byte mais significativo ao resultado decodificado
            decoded_string += chr((buffer >> (bit_counter - 8)) & 0xFF)
            # Reduz o contador de bits
            bit_counter -= 8

    return decoded_string

# Exemplo de uso:
input_string = "Ola mundo"
encoded_string = base64_encode(input_string)
print("String codificada em Base64:", encoded_string)

decoded_string = base64_decode(encoded_string)
print("String decodificada a partir de Base64:", decoded_string)