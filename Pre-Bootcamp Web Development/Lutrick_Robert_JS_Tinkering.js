var childHeight = 42 //Set kids height to 42 inches

//Function for detmining if the kid can ride this epic roller coaster or not
function displayIfChildIsAbleToRideTheRollerCoaster() 
{
    //Determine if the kid is tall enough to let on the ride
    if (childHeight > 52) {
        console.log("Get on that ride, kiddo!")
    } else {
        console.log("Sorry kiddo. Maybe next year.")
    }
}