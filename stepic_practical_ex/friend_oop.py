class Friends:
    def __init__(self, connections):
        tmp_conn = []
        for i in connections:
            if not tmp_conn or i not in tmp_conn:
                tmp_conn.append(i)
        self.conn = tmp_conn
        print(tmp_conn, connections)
        # raise NotImplementedError

    def add(self, connection):

        if not self.conn or connection not in self.conn:
            self.conn.append(connection)
        else:
            return False
        print(self.conn)
        return True
        # raise NotImplementedError

    def remove(self, connection):

        if self.conn and connection in self.conn:
            self.conn.remove(connection)
        else:
            return False
        print(self.conn)
        return True
        # raise NotImplementedError

    def names(self):

        self.names_cust = []

        for friend in self.conn:
            self.names_cust.extend(friend)

        print(set(self.names_cust))
        return set(self.names_cust)

        # raise NotImplementedError

    def connected(self, name):

        self.names_connected = []

        for friend in self.conn:
            if name in friend:
                self.names_connected.extend(friend)

        if self.names_connected:
            # print(name)
            self.names_connected = set(self.names_connected)
            self.names_connected = list(self.names_connected)
            self.names_connected.remove(name)

        print(self.names_connected)
        return set(self.names_connected)

        # raise NotImplementedError



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
