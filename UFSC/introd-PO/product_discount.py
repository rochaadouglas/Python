#Uma loja virtual concederá um desconto para seus clientes com base nos seus níveis de engajamento nas redes sociais da loja. Obtenha, via entrada do usuário, o nível de engajamento do cliente e o valor de sua compra (o valor precisa ser superior a R$100,00). Os níveis aceitos para desconto e os percentuais de desconto são os seguintes: seguidor → 5%; comentarista → 8%; fã → 12%. Caso o nível informado não seja nenhum dos anteriores ou o valor não satisfaça a condição, exiba uma mensagem avisando que o cliente não tem direito a desconto. Caso contrário, mostre o percentual de desconto obtido e o valor final da compra.
#A virtual store will give a discount to your customers with base in your engagement level at the social medias of store. with user input get your engagement level and your buying value (Value bigger than R$100,00). The level accepted and discount percent are: follower - 5%; commentarist - 8%; fan - 12%. If level report isn't any before or it value doesn't satisfy the condition, print a message saying that the custommer doesn't have a discount. If not, show the discount porcentage and your final buy value.
level_engagement = input('report your level of engagement: ')
buy_value = float(input('report your value of buy: '))
if level_engagement != 'follower' and level_engagement != 'commentarist' and level_engagement != 'fan' or buy_value <= 100:
    print('You do not have a discount.')
elif level_engagement == 'follower': #seguidor(a)
    product_discount = buy_value - (buy_value * 5/100)
    print(f'You have a 5% discount, you will buy: R${product_discount}')
elif level_engagement == 'commentarist': #comentarista
    product_discount = buy_value - (buy_value * 8/100)
    print(f'You have a 8% discount, you will buy: R${product_discount}')
elif level_engagement == 'fan': #fã
    product_discount = buy_value - (buy_value * 12/100)
    print(f'You have a 12% discount, you will buy: R${product_discount}')