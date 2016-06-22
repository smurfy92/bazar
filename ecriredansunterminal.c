void		ft_out(char *str)
{
	int fd = open("/dev/ttys001", O_WRONLY|O_NONBLOCK|O_NOCTTY);
	write(fd, str, ft_strlen(str));
}