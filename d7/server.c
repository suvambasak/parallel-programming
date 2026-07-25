#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include <sys/socket.h>
#include <sys/un.h>

#define SOCKET_PATH "hello.sock"
#define BUFFER_SIZE 1024

int main(void) {
  int server_fd, client_fd;
  struct sockaddr_un addr;
  char buffer[BUFFER_SIZE];
  char reply[BUFFER_SIZE];

  // Create socket
  server_fd = socket(AF_UNIX, SOCK_STREAM, 0);
  if (server_fd == -1) {
    perror("socket");
    exit(EXIT_FAILURE);
  }

  // Remove any previous socket file
  unlink(SOCKET_PATH);

  memset(&addr, 0, sizeof(addr));
  addr.sun_family = AF_UNIX;
  strncpy(addr.sun_path, SOCKET_PATH, sizeof(addr.sun_path) - 1);

  // Bind socket
  if (bind(server_fd, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
    perror("bind");
    close(server_fd);
    exit(EXIT_FAILURE);
  }

  // Listen for incoming connections
  if (listen(server_fd, 5) == -1) {
    perror("listen");
    close(server_fd);
    unlink(SOCKET_PATH);
    exit(EXIT_FAILURE);
  }

  printf("Server listening on %s\n", SOCKET_PATH);

  // Accept one client
  client_fd = accept(server_fd, NULL, NULL);
  if (client_fd == -1) {
    perror("accept");
    close(server_fd);
    unlink(SOCKET_PATH);
    exit(EXIT_FAILURE);
  }

  // Receive client's name
  ssize_t bytes = recv(client_fd, buffer, BUFFER_SIZE - 1, 0);
  if (bytes == -1) {
    perror("recv");
  } else {
    buffer[bytes] = '\0';

    printf("Received: %s\n", buffer);

    snprintf(reply, BUFFER_SIZE, "Hello %s", buffer);

    send(client_fd, reply, strlen(reply), 0);
  }

  close(client_fd);
  close(server_fd);

  unlink(SOCKET_PATH);

  return 0;
}
