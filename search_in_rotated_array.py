func call(lo, hi, x)
  if a[lo] < a[mi]
    slo, shi = lo, mi
    ulo, uhi = mi+1, hi
  else
    slo, shi = mi+1, hi
    ulo, uhi = lo, mi

  if slo<=x<=shi
    return call(slo, shi,x)
  return call(ulo, uhi,x)