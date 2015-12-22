function addPersonMethods(person){
  this.person=person;

 person.greet =function greetme(s){
      return console.log( s+ ", "+ "my name is "+ person.name);
    }
    person.namesake=function nameshake(b){
      if(person.name==b.name)
      return console.log("We have the same name, "+ b.name +" and I!");
      else {
        return console.log("We have different names, "+ b.name +" and I.");
      }

    }
    person.compareAge=function compareAge (b){
      if(person.age==b.age)
      return console.log("My name is "+person.name +" and I'm equally young as "+b.name);
      else if (person.age>b.age)
      return console.log("My name is "+person.name +" and I'm older than "+b.name);
      else {
         return console.log("My name is "+person.name +" and I'm younger than "+b.name);
      }
    }


return person;
   }
