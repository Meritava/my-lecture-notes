class iPhone {
    constructor(iPhone_version) {
        this.version = iPhone_version;  //the this is same as self in python, the version is an attribute, the iphone_version is an argument/parameter. so this line is saying that the attribute version should be assign the value iphone_version which is he argument passed into the parameter, i.e. the argumen passed in
        console.log(this.version);
    }

    getAlarm() {
        console.log("my alarm rings");
    }
}

const merit_iphone = new iPhone("14")
merit_iphone.getAlarm();

class iphone_new extends iPhone {
    //a class that inheits fim
}
//the constructor is same as the init method in python