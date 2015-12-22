

function keywordusage(text, keywords) {
  var n=new Array();
//  var text=new Array();
    //var text='Dive Into Python is a free book for experienced programmers';
   //var  keywords=['Python', 'python', 'scala'];
   for(var i=0;i < keywords.length;i++){
    if(text.indexOf(keywords[i])!=-1)
   n.push(true);
else
n.push(false);

}
return n;
}
function frequencies(text, wordlist){
	var n=new Object();
	a=wordlist;
	t=text;
	for(var i=0;i<a.length;i++){
var reg=new RegExp(a[i],"gi");
if (a[i]=='foo')
var del=(t.match(reg)|| []).length;

else if (a[i]=='bar')
var del1=(t.match(reg)|| []).length;
}
n["bar"]=del1;
n["foo"]=del;
return n;

}
function rotate(a,step){
  var step1 = step || 1;
if (step1>0){
   for(var i=0;i<step1;i++){
     var temp=a[a.length-1]
     for(var j=a.length-1;j>0;j--){
       a[j]=a[j-1];
       a[j-1]=temp;
     }
   }
}
 else if(step1<0){
    var n=(-1)*(step1)
   for(var i=0;i<n;i++){
     var temp=a[0]
     for(var j=0;j<a.length-1;j++){
       a[j]=a[j+1];
       a[j+1]=temp;
     }
   }
 }
 else{
   return a;
 }
   return a;

}

var a=[1,2,3,4];
console.log(rotate(a,15));
