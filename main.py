import spotipy, user, unify, misc

def main():
    print("Unify for Spotify v1.0")
    print("Created by Owen Ribera")

    un = input("Please input User 1's spotify ID: ")
    user1 = user.User(un, "dont need")

    un = input("Please input User 1's spotify ID: ")
    user2 = user.User(un, "dont need")

    union = unify.Unify(user1, user2)
    sim_artists = union.shared_artists()

    for i in sim_artists.keys():
        print(i)
main()