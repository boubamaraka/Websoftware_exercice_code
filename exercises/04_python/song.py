import json
import urllib
class Song:

    def __init__(self,name):

        self.name=name
        path="lastfm_subset"+"/"+self.name[2]+"/"+self.name[3]+"/"+self.name[4]+"/"
        self.name=path+name+".json"
        self.artist = "file"
        self.title = "not found"
        self.timestamp = "-1"
        self.track_id = name # should be whatever track_id was given
        self.tags = []
        self.similars = []
        try:

            json_data=open(self.name).read()
            wjdata = json.loads(json_data)
            self.tags=wjdata.get("tags",[])
            self.title=wjdata.get("title","not found")
            self.artist=wjdata.get("artist","file")
            self.timestamp=wjdata.get("timestamp","-1")
            self.track_id=wjdata.get("track_id",name)
            self.similars=wjdata.get("similars",[])
        except IOError:
            print ("The track Id cannot be found")


    def get_tags(self,limite=0):
        #print self.tags
        lst=[]
    #print wjdata["tags"]


        if limite>0:
            #max=None
            #label=None
            for i in self.tags:
                if  int(i[1])>=limite:
                    lst.append(i[0])
        else :
            for i in self.tags:
                lst.append(i[0])
            #print lst
        return lst

    def get_similars(self,limite=0):
        wjdata=self.similars
        lst=[]
        # me=0
         #print wjdata["tags"]
        if limite==0 :
             for i in wjdata:
                 lst.append(i[0])
                 #me=me+1
             #print me

        elif limite>0:

             for i in wjdata:
                 if i[1]>=limite:
                    lst.append(i[0])
             #print lst
        return lst
    def shared_tags(self,other_song_instance):

        val1=other_song_instance.get_tags()
        val2=self.get_tags()
        me=[]
        for i in val1:
            if i in val2:
                me.append(i)
        me=tuple(me)
        return me
    def combined_tags(self,other_song_instance):

        me=[]
        val1=other_song_instance.get_tags()
        val2=self.get_tags()
        for i in val1:
            if i in val2:
                continue
            else:
                val2.append(i)
        val2=tuple(val2)
        return val2




        #print val1
        #print val2
        #print val1






#val1="lastfm_subset"
#val="lastfm_subset/A/H/Q/TRAHQDQ128F421F629.json"
#add="TRAWHKS128F9330619"
#song1=song(add)
#song1.read()
#print song1.get_tags(3)
#rint song1.get_similars(0.90)
new=Song ('TRAWHKS12849330619')
#print new.get_tags()
some_song = Song('TRAWHKS128F9330619')
other_song = Song('TRANXZZ128F4230613')
print some_song.get_tags()
print some_song.get_tags(90)
print some_song.get_similars(0.9)
print other_song.get_tags()
print other_song.shared_tags(some_song)
print other_song.combined_tags(some_song)
#print add[2]
#print add[3]
#print add[4]
#print add1
#print val[0]
