def ordinalSuffix(num):
    snum = str(num)
    if snum[-2:] in ('1', '01'):
        return f'{snum}st'
    elif snum[-2:] == '2':
        return f'{snum}nd'
    elif snum[-2:] == '3':
        return f'{snum}rd'
    else:
        return f'{snum}th'

### Checks
assert ordinalSuffix(0) == '0th' 
assert ordinalSuffix(1) == '1st' 
assert ordinalSuffix(2) == '2nd' 
assert ordinalSuffix(3) == '3rd' 
assert ordinalSuffix(4) == '4th' 
assert ordinalSuffix(10) == '10th' 
assert ordinalSuffix(11) == '11th' 
assert ordinalSuffix(12) == '12th' 
assert ordinalSuffix(13) == '13th' 
assert ordinalSuffix(14) == '14th' 
assert ordinalSuffix(101) == '101st' 
