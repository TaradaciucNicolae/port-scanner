#Author: Taradaciuc Nicolae
import socket

tcp_and_udp_ports = {
    7: "Echo",
    135: "Microsoft RPC",
    161: "SNMP",
    389: "LDAP",
    445: "Microsoft DS SMB",
    464: "Kerberos password settings",
    596: "SMSD",
    2869: "UPnP -> ICSLAP",
    5060: "SIP"
}

# Dictionary for TCP connections
tcp_ports = {
    20: "FTP",
    21: "FTP",
    22: "SSH/SCP",
    23: "Telnet",
    25: "SMTP",
    80: "HTTP",
    88: "Kerberos",
    110: "POP3",
    139: "NetBIOS Session Service",
    143: "IMAP",
    194: "IRC",
    443: "HTTPS",
    445: "Microsoft DS SMB",
    636: "LDAP over SSL",
    1720: "H.323",
    3389: "RDP",
    5061: "SIP over TLS"
}


# Dictionary for popular UDP connections
udp_ports = {
    53: "DNS",
    67: "DHCP/BOOTP",
    68: "DHCP/BOOTP",
    69: "TFTP",
    123: "NTP",
    135: "Microsoft RPC",
    137: "NetBIOS",
    138: "NetBIOS",
    161: "SNMP",
    445: "Microsoft DS SMB",
    547: "DHCPv6",
    631: "IPP (Internet Printing Protocol)",
    1434: "MS SQL Monitor"
}

def scan_each_port(target_ip):

    counter = 0

    # We're creating a TCP socket
    Just_a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for each_tcp_and_udp_port in tcp_and_udp_ports:
        connection = Just_a_socket.connect_ex((target_ip, each_tcp_and_udp_port))
        if connection == 0:
            counter += 1
            print(f"Port {each_tcp_and_udp_port} (tcp/udp) is open -> {tcp_and_udp_ports[each_tcp_and_udp_port]}!")
        else:
            #print("not open")
            continue

    # We're creating a TCP socket
    Just_a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for each_tcp_port in tcp_ports:
        connection = Just_a_socket.connect_ex((target_ip, each_tcp_port))
        if connection == 0:
            counter += 1
            print(f"Port {each_tcp_port} (tcp) is open -> {tcp_ports[each_tcp_port]}!")
        else:
            #print("not open")
            continue


    # We're creating a UDP socket
    Just_a_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for each_udp_port in udp_ports:
        connection = Just_a_socket.connect_ex((target_ip, each_udp_port))
        if connection == 0:
            counter += 1
            print(f"Port {each_udp_port} (udp) is open -> {udp_ports[each_udp_port]}!")
        else:
            #print("not open")
            continue


    Just_a_socket.close()
    return counter


if __name__ == '__main__':

    print("Port-Scanner Project")

    target_ip = input("The IP address that we're scanning is:  ")

    counter = scan_each_port(target_ip)
    print(f"{counter} tcp ports are open!")
