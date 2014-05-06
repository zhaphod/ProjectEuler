#
# Problem 50
# Consecutive prime sum
# 
# The prime 41, can be written as the sum of six consecutive primes:
# 
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime 
# below one-hundred.
# 
# The longest sum of consecutive primes below one-thousand that adds 
# to a prime, contains 21 terms, and is equal to 953.
# 
# Which prime, below one-million, can be written as the sum of the 
# most consecutive primes?
#

function genPrimes(primes, n)
    for i in 2:n
        isPrime = true
        for j in 2:int(sqrt(i))
            if i % j == 0
                isPrime = false
                break
            end
        end
        if isPrime
            # println(i, " is prime")
            push!(primes, i)
        end
    end
    return
end

function getPrimeWithMaxSeq(primes)
    prime = 0
    len = 0
    for i in 1:length(primes)
        sum = 0
        for j in i:length(primes)#:i:-1
            sum += primes[j]
            if sum > primes[end]
                break
            end
            if sum in primes 
                if j - i > len
                    len = j - i
                    prime = sum
                end
            end
        end
    end
    return prime
end
    
primes = Uint64[]
genPrimes(primes, 1000000)

prime = getPrimeWithMaxSeq(primes)

println("prime = ", prime)