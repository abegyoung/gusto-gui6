def read_end(the_port, End):
  total_data=[];data=''
  while True:
    try:
      data=the_port.read(1).decode()
    except:
      break
    if End in data:
      total_data.append(data[:data.find(End)])
      break
    total_data.append(data)
    if len(total_data)>1:
      # check if end_of_data was split
      last_pair=total_data[-2]+total_data[-1]
      if End in last_pair:
        total_data[-2]=last_pair[:last_pair.find(End)]
        total_data.pop()
        break
  return ''.join(total_data)


def read_end_multi(the_port, End):
  total_data=[];data=''
  while True:
    try:
      data=the_port.read(10).decode()
    except:
      break
    if End in data:
      total_data.append(data[:data.find(End)])
      break
    total_data.append(data)
    if len(total_data)>1:
      # check if end_of_data was split
      last_pair=total_data[-2]+total_data[-1]
      if End in last_pair:
        total_data[-2]=last_pair[:last_pair.find(End)]
        total_data.pop()
        break
  return ''.join(total_data)


def recv_end(the_socket, End):
   total_data=[];data=''
   while True:
      try:
         data=the_socket.recv(8192)
      except:
         break
      if End in data:
         total_data.append(data[:data.find(End)])
         break
      total_data.append(data)
      if len(total_data)>1:
         #check if end_of_data was split
         last_pair=total_data[-2]+total_data[-1]
         if End in last_pair:
            total_data[-2]=last_pair[:last_pair.find(End)]
            total_data.pop()
            break
   return ''.join(total_data)

