per_cent = {"tbk" : 5.6, "skb": 5.9, "vtb": 4.28, "sber": 4.0} 

money = int(input("Введите сумму, которую хотите вложить: "))

tbk = float(per_cent.get("tbk"))
skb = float(per_cent.get("skb"))
vtb = float(per_cent.get("vtb"))
sber = float(per_cent.get("sber"))

deposit = [int(tbk * money / 100), int(skb * money / 100), int(vtb * money / 100), int(sber * money / 100)]

max_deposit = int(max(deposit))

print(deposit)
print("Максимальная сумма, которую вы можете заработать — ", max_deposit)
