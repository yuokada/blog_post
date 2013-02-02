<?php
assert_options(ASSERT_BAIL, true);
$ls = range(1, 100);
function factorial($x){
    assert(gettype($x) == "integer");
    if($x == 1){
        return 1;
    }else{
        return $x * factorial($x -1);
    }
}
var_dump(factorial(5));
var_dump(factorial(5.5));
var_dump(factorial(6));
// range の実装がえげつないほど緩いｗ
//var_dump(range(1, 10.0, 0.5));
//var_dump(range(1, "10.0"));
