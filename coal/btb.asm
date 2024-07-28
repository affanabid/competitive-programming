.model small
.stack 100h
.386
.data
	prompt db 'Enter bin: $'
	output db 10, 13, 'bin: $'
.code
main proc
	mov ax, @data
	mov ds, ax

	lea dx, prompt
	mov ah, 9
	int 21h

	mov cx, 8
	
inp:	mov ah, 1
	int 21h
	
	SHL Bl, 1

	SUB al, 48

	OR Bl, Al

	dec cx
	jnz inp

;output
	lea dx, output
	mov ah, 9
	int 21h

	mov cx, 8
	
outp:	SHL Bl, 1
	JC one

	mov Dl, '0'
	mov ah, 2
	int 21h
	jmp aa

one:	mov Dl, '1'
	mov ah, 2
	int 21h

aa:	dec cx
	jnz outp

exit:	mov ah, 4Ch
	int 21h
	
main endp
end main