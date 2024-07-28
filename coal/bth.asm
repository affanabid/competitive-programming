.model small
.stack 100h
.386
.data
	prompt db 'Enter bin: $'
	output db 10, 13, 'hex: $'
.code
main proc
	mov ax, @data
	mov ds, ax

	lea dx, prompt
	mov ah, 9
	int 21h
;input
	mov cx, 16

inp:	mov ah, 01
	int 21h
	
	SUB Al, 48

	SHL Bx, 1

	OR Bl, Al

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
	JA letter

	ADD Dl, 48
	JMP aa

letter:	ADD Dl, 55

aa:	mov ah, 2
	int 21h

	dec cx
	jnz outp

exit:	mov ah, 4Ch
	int 21h
	
main endp
end main