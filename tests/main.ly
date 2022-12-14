struct Person {
  name: char[32];
  age: int;
  height: int;
}

struct Car { model: char[32]; date: int; }

// No params
def func1() { pass; }

// No return
def func2(a_val: int) { pass; }

// Params anf return
def func3(a: int): int { pass; }

// With body
def func4(a: i32, b: char[32]): i32 {
  if(a > 3){
	b = "test";
  }elif (a < 3) {
	b = """
	multiline string
	testing
	""";
  }

  return 0;
}

// Main function
def main(): i32 {
  
  // function call test
  params_func(34, "test");

  // variable test
  var age: i32 = 0;
  var ages: i32[20];

  // re-assign test
  age = 90;
  
  ages[0] = 4;
  ages[1] = 3;

  // loops

  while a < 20 {
	break;
	continue;
  }
  
  v = name.age();
  n = person.names[0];

  return;
}
