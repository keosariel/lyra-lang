struct Person {
  name: char[32];
  age: i32;
  height: i32;
}

struct Car { model: char[32]; date: i32; }
struct Point {x: i32; y:i32;}
// No params
def func1() { pass; }

// No return
def func2(a_val: i32): i32 { pass; }

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

  var p: Point = Point(21, 44);

  var va: Point;
  va.x = 43;
  va.y = 44;

  // variable test
  var age: i32 = 1 + 4;
  var ages: i32[20];
  var b: i32 = 1 << 2;
  var g: f32 = -1.3;
  // function call test
  func2(age);
  
  var nums: i32[5][2] = [];

  nums[0] = [1,2,3,4,5];
  // re-assign test
  age = 90;
  
//  ages[0] = 4;
//  ages[1] = 3;

  // loops

  while age == 5 {
	var xx: i32 = 4;
	break;
	continue;
  }

  // func2(xx); xx is out of scope
  
  b = func2(33);
  // n = person.names[0];

  return;
}
