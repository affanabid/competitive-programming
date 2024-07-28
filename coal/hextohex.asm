.model small
.stack 100h
.386
.data
	prompt db 'Enter a hex number: $'
	output db 10, 13, 'The hex is: $'
	space db 100 dup('$')
.code
main proc
	mov ax, @data
	mov ds, ax

;input
	lea dx, prompt
	mov ah, 9
	int 21h

	XOR bx, bx
	mov cx, 4

inp:	mov ah, 01
	int 21h

	
	
	cmp al, '9'
	ja letter1

	sub al, 48

letter1:sub al, 55

	ROL Bx, 4

	OR bl, al
	
	dec cx
	jnz inp

;output
	lea dx, output
	mov ah, 9
	int 21h

	mov cx, 4

outp:	ROL Bx, 4
	
	mov Dl, Bl

	AND Dl, 0Fh

	cmp Dl, 9
	ja letter2	
	
	add dl, 48

letter2:add dl, 55

	mov ah, 2
	int 21h

	dec cx
	jnz outp


exit:	mov ah, 4Ch
	int 21h
	
main endp
end main

