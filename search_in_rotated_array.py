if left is sorted pick it to check,
  clo, chi = lo, mi
  olo, ohi = mi, hi
else
  clo, chi = mi, hi
  olo, ohi = lo, mi

if clo<x<chi
  return call(clo,chi)
return call(olo, ohi)
