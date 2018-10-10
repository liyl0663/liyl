import dns.resolver

domain = input('Please input an domain:')
A = dns.resolver.query(domain,'A')
MX = dns.resolver.query(domain,'MX')
for i in A.response.answer:
    #print(i)
    for j in i.items:
        print(j)
for i in MX:
    print(
        'MX preference =',i.preference,
        'mail exchanger =',i.exchange
    )

