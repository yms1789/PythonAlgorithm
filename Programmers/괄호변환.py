def solution(p):
    # case 1
    if p == '':
        return ''

    def balanceParen(paren):
        if paren == '':
            return paren
        u = ''
        v = ''
        lparen = 0
        rparen = 0
        for a in paren:
            u += a
            if a == '(':
                lparen += 1
            else:
                rparen += 1
            if lparen == rparen:
                break
        v = paren[len(u):]
        if corrParen(u):
            return u + balanceParen(v)
        else:
            tmp = '('  # 4-1
            tmp += balanceParen(v)  # 4-2
            tmp += ')'  # 4-3
            for rem in u[1:len(u) - 1]:  # 4-4
                if rem == '(':
                    tmp += ')'
                else:
                    tmp += '('
            return tmp  # 4-5

    def corrParen(paren):
        if paren[0] == ')':
            return False
        lparen = 0
        rparen = 0
        for a in paren:
            if a == '(':
                lparen += 1
            else:
                rparen += 1
            if rparen > lparen:
                return False
        if rparen != lparen:
            return False
        return True

    res = corrParen(p)
    if res:
        return p
    else:
        return balanceParen(p)
print(solution('()))((()'))