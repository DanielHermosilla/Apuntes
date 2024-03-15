
>El concepto de transacción es el equivalente computacional de un contrato legal. Imagínese una sociedad sin ley de contratos. Eso es lo que sería un sistema computacional sin transacciones. Si nada nunca sale mal, los contratos son sólo un overhead. Pero si algo no funciona bien, el contrato especifica como limpiar la situación.

En sintaxis estándar en *postgresSQL* sería: 

```SQL 
START TRANSACTION; 
	INSERT INTO Gasto VALUES 
		(787369382, 'Noruega')
	UPDATE Cuenta SET saldo_clp=175000, saldo_usd=-268.29 WHERE numero=787369382 
COMMIT; 
```

