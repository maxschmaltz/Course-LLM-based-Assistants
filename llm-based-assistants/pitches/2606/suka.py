from multi_agent.tools import read_last_ticket, send_reply_to_ticket, return_ticket_suka




for i in range(20):
    ticket = read_last_ticket()
    asnwer = return_ticket_suka(ticket)
    send_reply_to_ticket(ticket, asnwer, close=False)
    print("suka")