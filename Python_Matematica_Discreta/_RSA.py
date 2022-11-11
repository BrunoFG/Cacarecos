# RSA = Rivest-Shamir-Adleman encryption
# 1) Gerar um par de chaves -> uma pública e uma privada
#       Procurar 2 primos grandes (aleatórios) p e q.
#       teste de primo ordem n^12, transformada discreta de fourier (DFT) ordem n^2, (FFT) ordem n.log(n)
# 2) Testes estatísticos
#       Teste de Fermat -> a^n-1 congruente com 1 (mod n)
#       Teste de Miller-Rabin -> a^n-1 congruente com 1 (mod n)

# 1)
# n = p.q
# phi(n) = (p-1).(q-1)
# Escolher E tal que MDC(E, phi(n))=1
# Calcula d tal que E.d congruente com 1 (mod phi(n))
# d = pow(E, -1, phi(n))
# Divulga (n,e)
# Privado (d)

# 2)
# Para enviar mensagem
# Y cong X^E (mod n) --> pow(X, E, n)
# Envia Y para o usuário
# 3) Para decifrar
# R cong Y^d (mod n)
# R cong X^(ed) (mod n)
# ed cong 1 + k.phi(n)
# R cong X^(1+k.phi(n)) cong x(x^phi(n))^k (mod n)

# Teorema de Euler
# MDC(x,n)=1 -> X^phi(n) cong 1 (mod n)
# R cong 

#def testeDeMillerRabin(n):