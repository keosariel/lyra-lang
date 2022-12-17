struct Person {
  name: char[32];
  age: int;
  height: int;
}

struct Car { model: char[32]; date: int; }

// No params
def func1() { pass; }

// No return
def func2(a_val: i32) { pass; }

// Params anf return
def func3(a: i64): i64 { pass; }

// With body
// def func4(a: i32, b: char[32]): i32 {
//  if(a > 3){
//	b = "test";
//  }elif (a < 3) {
//	b = """
//	multiline string
//	testing
//	""";
// }

///  return 0;
//}

// Main function
def main(): i64 {
  
  // function call test
  func2(34);

  // variable test
  var age: i32 = 1 + 4;
  var ages: i32[20];
  var b: i32 = 1 << 2;
  var g: f32 = -1.3;
  // function call test
  func2(age);

  // re-assign test
  age = 90;
  
//  ages[0] = 4;
//  ages[1] = 3;

  // loops

  while age == 5 {
	age = r;
	break;
	continue;
  }
  
  v = name.age();
  n = person.names[0];

  return;
}
