﻿f r o m   d j a n g o . s h o r t c u t s   i m p o r t   r e n d e r ,   g e t _ o b j e c t _ o r _ 4 0 4 ,   r e d i r e c t 
 
 f r o m   d j a n g o . c o n t r i b . a u t h . d e c o r a t o r s   i m p o r t   l o g i n _ r e q u i r e d ,   u s e r _ p a s s e s _ t e s t 
 
 f r o m   d j a n g o . h t t p   i m p o r t   H t t p R e s p o n s e ,   H t t p R e s p o n s e F o r b i d d e n ,   J s o n R e s p o n s e 
 
 f r o m   d j a n g o . d b . m o d e l s   i m p o r t   S u m ,   C o u n t ,   Q 
 
 f r o m   d j a n g o . c o r e . p a g i n a t o r   i m p o r t   P a g i n a t o r 
 
 f r o m   d j a n g o . c o n t r i b   i m p o r t   m e s s a g e s 
 
 f r o m   u s e r s . m o d e l s   i m p o r t   C u s t o m U s e r ,   E m p l o y e r P r o f i l e ,   E m p l o y e e P r o f i l e ,   L o c a t i o n 
 
 f r o m   t r i p s . m o d e l s   i m p o r t   T r i p ,   C a r b o n C r e d i t 
 
 f r o m   d j a n g o . u t i l s   i m p o r t   t i m e z o n e 
 
 i m p o r t   c s v 
 
 i m p o r t   i o 
 
 f r o m   d j a n g o . u r l s   i m p o r t   r e v e r s e 
 
 f r o m   d e c i m a l   i m p o r t   D e c i m a l 
 
 
 
 #   I m p o r t   m a r k e t p l a c e   m o d e l s   i f   n e e d e d 
 
 f r o m   m a r k e t p l a c e . m o d e l s   i m p o r t   M a r k e t O f f e r ,   M a r k e t p l a c e T r a n s a c t i o n 
 
 
 
 d e f   i s _ s u p e r _ a d m i n ( u s e r ) : 
 
         r e t u r n   u s e r . i s _ a u t h e n t i c a t e d   a n d   u s e r . i s _ s u p e r _ a d m i n 
 
 
 
 @ l o g i n _ r e q u i r e d 
 
 @ u s e r _ p a s s e s _ t e s t ( i s _ s u p e r _ a d m i n ) 
 
 d e f   d a s h b o a r d ( r e q u e s t ) : 
 
         " " " 
 
         A d m i n   d a s h b o a r d   v i e w   -   s h o w s   s y s t e m   s t a t i s t i c s 
 
         " " " 
 
         #   C o u n t   t o t a l   u s e r s ,   t r i p s ,   a n d   c a r b o n   c r e d i t s 
 
         t o t a l _ u s e r s   =   C u s t o m U s e r . o b j e c t s . c o u n t ( ) 
 
         e m p l o y e r s   =   E m p l o y e r P r o f i l e . o b j e c t s . c o u n t ( ) 
 
         e m p l o y e e s   =   E m p l o y e e P r o f i l e . o b j e c t s . c o u n t ( ) 
 
         b a n k _ a d m i n s   =   C u s t o m U s e r . o b j e c t s . f i l t e r ( i s _ b a n k _ a d m i n = T r u e ) . c o u n t ( ) 
 
         s u p e r _ a d m i n s   =   C u s t o m U s e r . o b j e c t s . f i l t e r ( i s _ s u p e r _ a d m i n = T r u e ) . c o u n t ( ) 
 
         p e n d i n g _ a p p r o v a l   =   E m p l o y e r P r o f i l e . o b j e c t s . f i l t e r ( a p p r o v e d = F a l s e ) . c o u n t ( ) 
 
         
 
         #   G e t   f r o m   t h e   t r i p   a n d   c a r b o n   c r e d i t   m o d e l s 
 
         t o t a l _ t r i p s   =   T r i p . o b j e c t s . c o u n t ( ) 
 
         
 
         #   C o u n t   n e w   u s e r s   i n   l a s t   3 0   d a y s 
 
         t h i r t y _ d a y s _ a g o   =   t i m e z o n e . n o w ( )   -   t i m e z o n e . t i m e d e l t a ( d a y s = 3 0 ) 
 
         n e w _ u s e r _ c o u n t   =   C u s t o m U s e r . o b j e c t s . f i l t e r ( d a t e _ j o i n e d _ _ g t e = t h i r t y _ d a y s _ a g o ) . c o u n t ( ) 
 
         
 
         #   C o u n t   r e c e n t   t r i p s   i n   l a s t   7   d a y s 
 
         s e v e n _ d a y s _ a g o   =   t i m e z o n e . n o w ( )   -   t i m e z o n e . t i m e d e l t a ( d a y s = 7 ) 
 
         r e c e n t _ t r i p _ c o u n t   =   T r i p . o b j e c t s . f i l t e r ( s t a r t _ t i m e _ _ g t e = s e v e n _ d a y s _ a g o ) . c o u n t ( ) 
 
         
 
         #   G e t   c a r b o n   c r e d i t s   w i t h   p r o p e r   f o r m a t t i n g 
 
         t o t a l _ c r e d i t s _ r a w   =   C a r b o n C r e d i t . o b j e c t s . a g g r e g a t e ( S u m ( ' a m o u n t ' ) ) [ ' a m o u n t _ _ s u m ' ]   o r   0 
 
         t o t a l _ c r e d i t s   =   r o u n d ( f l o a t ( t o t a l _ c r e d i t s _ r a w ) ,   2 ) 
 
         
 
         #   G e t   p e n d i n g   e m p l o y e r s   f o r   a p p r o v a l 
 
         p e n d i n g _ e m p l o y e r s   =   E m p l o y e r P r o f i l e . o b j e c t s . f i l t e r ( a p p r o v e d = F a l s e ) . s e l e c t _ r e l a t e d ( ' u s e r ' ) . o r d e r _ b y ( ' - c r e a t e d _ a t ' ) [ : 5 ] 
 
         
 
         #   G e t   r e c e n t   t r i p s   f o r   t h e   d a s h b o a r d 
 
         r e c e n t _ t r i p s   =   T r i p . o b j e c t s . s e l e c t _ r e l a t e d ( 
 
                 ' e m p l o y e e ' ,   ' e m p l o y e e _ _ u s e r ' ,   ' e m p l o y e e _ _ e m p l o y e r ' ,   ' s t a r t _ l o c a t i o n ' ,   ' e n d _ l o c a t i o n ' 
 
         ) . o r d e r _ b y ( ' - s t a r t _ t i m e ' ) [ : 1 0 ] 
 
         
 
         c o n t e x t   =   { 
 
                 ' t o t a l _ u s e r s ' :   t o t a l _ u s e r s , 
 
                 ' e m p l o y e r s ' :   e m p l o y e r s , 
 
                 ' e m p l o y e e s ' :   e m p l o y e e s , 
 
                 ' e m p l o y e e _ c o u n t ' :   e m p l o y e e s , 
 
                 ' e m p l o y e r _ c o u n t ' :   e m p l o y e r s , 
 
                 ' b a n k _ a d m i n _ c o u n t ' :   b a n k _ a d m i n s , 
 
                 ' s u p e r _ a d m i n _ c o u n t ' :   s u p e r _ a d m i n s , 
 
                 ' p e n d i n g _ a p p r o v a l ' :   p e n d i n g _ a p p r o v a l , 
 
                 ' p e n d i n g _ a p p r o v a l _ c o u n t ' :   p e n d i n g _ a p p r o v a l , 
 
                 ' t o t a l _ t r i p s ' :   t o t a l _ t r i p s , 
 
                 ' t r i p _ c o u n t ' :   t o t a l _ t r i p s , 
 
                 ' r e c e n t _ t r i p _ c o u n t ' :   r e c e n t _ t r i p _ c o u n t , 
 
                 ' n e w _ u s e r _ c o u n t ' :   n e w _ u s e r _ c o u n t , 
 
                 ' t o t a l _ c r e d i t s ' :   t o t a l _ c r e d i t s , 
 
                 ' p e n d i n g _ e m p l o y e r s ' :   p e n d i n g _ e m p l o y e r s , 
 
                 ' r e c e n t _ t r i p s ' :   r e c e n t _ t r i p s , 
 
         } 
 
         
 
         r e t u r n   r e n d e r ( r e q u e s t ,   ' a d m i n / d a s h b o a r d . h t m l ' ,   c o n t e x t ) 
 
 
 
 @ l o g i n _ r e q u i r e d 
 
 @ u s e r _ p a s s e s _ t e s t ( i s _ s u p e r _ a d m i n ) 
 
 d e f   d a s h b o a r d _ r e c e n t _ t r i p s ( r e q u e s t ) : 
 
         " " " 
 
         H T M X - c o m p a t i b l e   v i e w   t h a t   r e t u r n s   r e c e n t   t r i p s   f o r   t h e   a d m i n   d a s h b o a r d 
 
         " " " 
 
         #   G e t   r e c e n t   t r i p s   w i t h   e m p l o y e e   a n d   l o c a t i o n   d e t a i l s 
 
         t r i p s   =   T r i p . o b j e c t s . s e l e c t _ r e l a t e d ( 
 
                 ' e m p l o y e e ' ,   ' e m p l o y e e _ _ u s e r ' ,   ' s t a r t _ l o c a t i o n ' ,   ' e n d _ l o c a t i o n ' 
 
         ) . o r d e r _ b y ( ' - s t a r t _ t i m e ' ) [ : 1 0 ] 
 
         
 
         #   G e t   t r a n s p o r t   m o d e s   f o r   d i s p l a y 
 
         t r a n s p o r t _ m o d e s   =   T r i p . T R A N S P O R T _ M O D E S 
 
         
 
         c o n t e x t   =   { 
 
                 ' t r i p s ' :   t r i p s , 
 
                 ' t r a n s p o r t _ m o d e s ' :   t r a n s p o r t _ m o d e s , 
 
         } 
 
         
 
         r e t u r n   r e n d e r ( r e q u e s t ,   ' a d m i n / p a r t i a l s / r e c e n t _ t r i p s . h t m l ' ,   c o n t e x t ) 
 
 
 
 @ l o g i n _ r e q u i r e d 
 
 @ u s e r _ p a s s e s _ t e s t ( i s _ s u p e r _ a d m i n ) 
 
 d e f   u s e r s _ l i s t ( r e q u e s t ) : 
 
         " " " 
 
         A d m i n   u s e r s   m a n a g e m e n t   v i e w   w i t h   e n h a n c e d   f i l t e r i n g   a n d   s e a r c h 
 
         " " " 
 
         #   G e t   f i l t e r   p a r a m e t e r s 
 
         r o l e _ f i l t e r   =   r e q u e s t . G E T . g e t ( ' r o l e ' ,   ' ' ) 
 
         s t a t u s _ f i l t e r   =   r e q u e s t . G E T . g e t ( ' s t a t u s ' ,   ' ' ) 
 
         s e a r c h _ q u e r y   =   r e q u e s t . G E T . g e t ( ' s e a r c h ' ,   ' ' ) 
 
         s o r t _ b y   =   r e q u e s t . G E T . g e t ( ' s o r t ' ,   ' d a t e _ j o i n e d ' ) 
 
         s o r t _ d i r   =   r e q u e s t . G E T . g e t ( ' d i r ' ,   ' d e s c ' ) 
 
         
 
         #   S t a r t   w i t h   a l l   u s e r s 
 
         u s e r s _ q u e r y s e t   =   C u s t o m U s e r . o b j e c t s . a l l ( ) 
 
         
 
         #   A p p l y   r o l e   f i l t e r 
 
         i f   r o l e _ f i l t e r : 
 
                 i f   r o l e _ f i l t e r   = =   ' s u p e r _ a d m i n ' : 
 
                         u s e r s _ q u e r y s e t   =   u s e r s _ q u e r y s e t . f i l t e r ( i s _ s u p e r _ a d m i n = T r u e ) 
 
                 e l i f   r o l e _ f i l t e r   = =   ' b a n k _ a d m i n ' : 
 
                         u s e r s _ q u e r y s e t   =   u s e r s _ q u e r y s e t . f i l t e r ( i s _ b a n k _ a d m i n = T r u e ) 
 
                 e l i f   r o l e _ f i l t e r   = =   ' e m p l o y e r ' : 
 
                         u s e r s _ q u e r y s e t   =   u s e r s _ q u e r y s e t . f i l t e r ( i s _ e m p l o y e r = T r u e ) 
 
                 e l i f   r o l e _ f i l t e r   = =   ' e m p l o y e e ' : 
 
                         u s e r s _ q u e r y s e t   =   u s e r s _ q u e r y s e t . f i l t e r ( i s _ e m p l o y e e = T r u e ) 
 
         
 
         #   A p p l y   s t a t u s   f i l t e r 
 
         i f   s t a t u s _ f i l t e r : 
 
                 i f   s t a t u s _ f i l t e r   = =   ' a p p r o v e d ' : 
 
                         u s e r s _ q u e r y s e t   =   u s e r s _ q u e r y s e t . f i l t e r ( a p p r o v e d = T r u e ) 
 
                 e l i f   s t a t u s _ f i l t e r   = =   ' p e n d i n g ' : 
 
                         u s e r s _ q u e r y s e t   =   u s e r s _ q u e r y s e t . f i l t e r ( a p p r o v e d = F a l s e ) 
 
         
 
         #   A p p l y   s e a r c h   f i l t e r 
 
         i f   s e a r c h _ q u e r y : 
 
                 u s e r s _ q u e r y s e t   =   u s e r s _ q u e r y s e t . f i l t e r ( 
 
                         Q ( e m a i l _ _ i c o n t a i n s = s e a r c h _ q u e r y )   | 
 
                         Q ( f i r s t _ n a m e _ _ i c o n t a i n s = s e a r c h _ q u e r y )   | 
 
                         Q ( l a s t _ n a m e _ _ i c o n t a i n s = s e a r c h _ q u e r y )   | 
 
                         Q ( e m p l o y e r _ p r o f i l e _ _ c o m p a n y _ n a m e _ _ i c o n t a i n s = s e a r c h _ q u e r y ) 
 
                 ) . d i s t i n c t ( ) 
 
         
 
         #   A p p l y   s o r t i n g 
 
         i f   s o r t _ b y   = =   ' n a m e ' : 
 
                 o r d e r _ f i e l d   =   ' f i r s t _ n a m e '   i f   s o r t _ d i r   = =   ' a s c '   e l s e   ' - f i r s t _ n a m e ' 
 
         e l i f   s o r t _ b y   = =   ' e m a i l ' : 
 
                 o r d e r _ f i e l d   =   ' e m a i l '   i f   s o r t _ d i r   = =   ' a s c '   e l s e   ' - e m a i l ' 
 
         e l i f   s o r t _ b y   = =   ' r o l e ' : 
 
                 #   S o r t i n g   b y   r o l e   i s   c o m p l e x   -   f a l l b a c k   t o   d a t e   j o i n e d 
 
                 o r d e r _ f i e l d   =   ' - d a t e _ j o i n e d ' 
 
         e l s e :     #   d e f a u l t   t o   d a t e _ j o i n e d 
 
                 o r d e r _ f i e l d   =   ' d a t e _ j o i n e d '   i f   s o r t _ d i r   = =   ' a s c '   e l s e   ' - d a t e _ j o i n e d ' 
 
         
 
         u s e r s _ q u e r y s e t   =   u s e r s _ q u e r y s e t . o r d e r _ b y ( o r d e r _ f i e l d ) 
 
         
 
         #   P r e f e t c h   r e l a t e d   p r o f i l e s   f o r   o p t i m i z a t i o n 
 
         u s e r s _ q u e r y s e t   =   u s e r s _ q u e r y s e t . p r e f e t c h _ r e l a t e d ( 
 
                 ' e m p l o y e r _ p r o f i l e ' ,   
 
                 ' e m p l o y e e _ p r o f i l e ' ,   
 
                 ' e m p l o y e e _ p r o f i l e _ _ e m p l o y e r ' 
 
         ) 
 
         
 
         #   P a g i n a t i o n 
 
         p a g e _ n u m b e r   =   r e q u e s t . G E T . g e t ( ' p a g e ' ,   1 ) 
 
         p a g i n a t o r   =   P a g i n a t o r ( u s e r s _ q u e r y s e t ,   2 0 )     #   2 0   u s e r s   p e r   p a g e 
 
         u s e r s   =   p a g i n a t o r . g e t _ p a g e ( p a g e _ n u m b e r ) 
 
         
 
         c o n t e x t   =   { 
 
                 ' u s e r s ' :   u s e r s , 
 
                 ' r o l e _ f i l t e r ' :   r o l e _ f i l t e r , 
 
                 ' s t a t u s _ f i l t e r ' :   s t a t u s _ f i l t e r , 
 
                 ' s e a r c h _ q u e r y ' :   s e a r c h _ q u e r y , 
 
                 ' s o r t _ b y ' :   s o r t _ b y , 
 
                 ' s o r t _ d i r ' :   s o r t _ d i r , 
 
                 ' p a g e _ o b j ' :   u s e r s , 
 
                 ' t o t a l _ u s e r s ' :   u s e r s _ q u e r y s e t . c o u n t ( ) , 
 
         } 
 
         
 
         r e t u r n   r e n d e r ( r e q u e s t ,   ' a d m i n / u s e r s . h t m l ' ,   c o n t e x t ) 
 
 
 
 @ l o g i n _ r e q u i r e d 
 
 @ u s e r _ p a s s e s _ t e s t ( i s _ s u p e r _ a d m i n ) 
 
 d e f   u s e r _ d e t a i l ( r e q u e s t ,   u s e r _ i d ) : 
 
         " " " 
 
         D e t a i l e d   v i e w   f o r   a   s p e c i f i c   u s e r 
 
         " " " 
 
         u s e r   =   g e t _ o b j e c t _ o r _ 4 0 4 ( C u s t o m U s e r ,   i d = u s e r _ i d ) 
 
         
 
         #   G e t   u s e r ' s   p r o f i l e   b a s e d   o n   r o l e 
 
         p r o f i l e   =   N o n e 
 
         i f   u s e r . i s _ e m p l o y e r : 
 
                 p r o f i l e   =   g e t a t t r ( u s e r ,   ' e m p l o y e r _ p r o f i l e ' ,   N o n e ) 
 
         e l i f   u s e r . i s _ e m p l o y e e : 
 
                 p r o f i l e   =   g e t a t t r ( u s e r ,   ' e m p l o y e e _ p r o f i l e ' ,   N o n e ) 
 
         
 
         #   G e t   u s e r ' s   t r i p s   i f   t h e y ' r e   a n   e m p l o y e e 
 
         t r i p s   =   [ ] 
 
         i f   u s e r . i s _ e m p l o y e e   a n d   h a s a t t r ( u s e r ,   ' e m p l o y e e _ p r o f i l e ' ) : 
 
                 t r i p s   =   T r i p . o b j e c t s . f i l t e r ( e m p l o y e e = u s e r . e m p l o y e e _ p r o f i l e ) . o r d e r _ b y ( ' - s t a r t _ t i m e ' ) [ : 1 0 ] 
 
         
 
         #   G e t   u s e r ' s   l o c a t i o n s 
 
         l o c a t i o n s   =   L o c a t i o n . o b j e c t s . f i l t e r ( c r e a t e d _ b y = u s e r ) 
 
         
 
         #   G e t   c a r b o n   c r e d i t s   f o r   t h i s   u s e r 
 
         c r e d i t s   =   N o n e 
 
         i f   u s e r . i s _ e m p l o y e e   a n d   h a s a t t r ( u s e r ,   ' e m p l o y e e _ p r o f i l e ' ) : 
 
                 c r e d i t s   =   C a r b o n C r e d i t . o b j e c t s . f i l t e r ( o w n e r _ t y p e = ' e m p l o y e e ' ,   o w n e r _ i d = u s e r . e m p l o y e e _ p r o f i l e . i d ) 
 
         
 
         c o n t e x t   =   { 
 
                 ' u s e r _ d e t a i l ' :   u s e r , 
 
                 ' p r o f i l e ' :   p r o f i l e , 
 
                 ' t r i p s ' :   t r i p s , 
 
                 ' l o c a t i o n s ' :   l o c a t i o n s , 
 
                 ' c r e d i t s ' :   c r e d i t s , 
 
         } 
 
         
 
         r e t u r n   r e n d e r ( r e q u e s t ,   ' a d m i n / u s e r _ d e t a i l . h t m l ' ,   c o n t e x t ) 
 
 
 
 @ l o g i n _ r e q u i r e d 
 
 @ u s e r _ p a s s e s _ t e s t ( i s _ s u p e r _ a d m i n ) 
 
 d e f   a p p r o v e _ u s e r ( r e q u e s t ,   u s e r _ i d ) : 
 
         " " " 
 
         A p p r o v e   a   u s e r   a c c o u n t 
 
         " " " 
 
         i f   r e q u e s t . m e t h o d   ! =   ' P O S T ' : 
 
                 r e t u r n   H t t p R e s p o n s e F o r b i d d e n ( " M e t h o d   n o t   a l l o w e d " ) 
 
         
 
         u s e r   =   g e t _ o b j e c t _ o r _ 4 0 4 ( C u s t o m U s e r ,   i d = u s e r _ i d ) 
 
         u s e r . a p p r o v e d   =   T r u e 
 
         u s e r . s a v e ( ) 
 
         
 
         #   A l s o   a p p r o v e   p r o f i l e   i f   e x i s t s 
 
         i f   u s e r . i s _ e m p l o y e r   a n d   h a s a t t r ( u s e r ,   ' e m p l o y e r _ p r o f i l e ' ) : 
 
                 u s e r . e m p l o y e r _ p r o f i l e . a p p r o v e d   =   T r u e 
 
                 u s e r . e m p l o y e r _ p r o f i l e . s a v e ( ) 
 
         e l i f   u s e r . i s _ e m p l o y e e   a n d   h a s a t t r ( u s e r ,   ' e m p l o y e e _ p r o f i l e ' ) : 
 
                 u s e r . e m p l o y e e _ p r o f i l e . a p p r o v e d   =   T r u e 
 
                 u s e r . e m p l o y e e _ p r o f i l e . s a v e ( ) 
 
         
 
         m e s s a g e s . s u c c e s s ( r e q u e s t ,   f " U s e r   { u s e r . e m a i l }   h a s   b e e n   a p p r o v e d . " ) 
 
         
 
         #   R e t u r n   p a r t i a l   H T M L   f o r   H T M X   o r   r e d i r e c t 
 
         i f   r e q u e s t . h e a d e r s . g e t ( ' H X - R e q u e s t ' ) : 
 
                 r e t u r n   r e n d e r ( r e q u e s t ,   ' a d m i n / p a r t i a l s / u s e r _ r o w . h t m l ' ,   { ' u s e r ' :   u s e r } ) 
 
         
 
         r e t u r n   r e d i r e c t ( ' a d m i n _ u s e r s ' ) 
 
 
 
 @ l o g i n _ r e q u i r e d 
 
 @ u s e r _ p a s s e s _ t e s t ( i s _ s u p e r _ a d m i n ) 
 
 d e f   r e j e c t _ u s e r ( r e q u e s t ,   u s e r _ i d ) : 
 
         " " " 
 
         R e j e c t   a   u s e r   a c c o u n t 
 
         " " " 
 
         i f   r e q u e s t . m e t h o d   ! =   ' P O S T ' : 
 
                 r e t u r n   H t t p R e s p o n s e F o r b i d d e n ( " M e t h o d   n o t   a l l o w e d " ) 
 
         
 
         u s e r   =   g e t _ o b j e c t _ o r _ 4 0 4 ( C u s t o m U s e r ,   i d = u s e r _ i d ) 
 
         
 
         #   M a r k   a s   r e j e c t e d   b y   s e t t i n g   a p p r o v e d   t o   F a l s e 
 
         u s e r . a p p r o v e d   =   F a l s e 
 
         u s e r . s a v e ( ) 
 
         
 
         #   A l s o   u p d a t e   p r o f i l e   i f   e x i s t s 
 
         i f   u s e r . i s _ e m p l o y e r   a n d   h a s a t t r ( u s e r ,   ' e m p l o y e r _ p r o f i l e ' ) : 
 
                 u s e r . e m p l o y e r _ p r o f i l e . a p p r o v e d   =   F a l s e 
 
                 u s e r . e m p l o y e r _ p r o f i l e . s a v e ( ) 
 
         e l i f   u s e r . i s _ e m p l o y e e   a n d   h a s a t t r ( u s e r ,   ' e m p l o y e e _ p r o f i l e ' ) : 
 
                 u s e r . e m p l o y e e _ p r o f i l e . a p p r o v e d   =   F a l s e 
 
                 u s e r . e m p l o y e e _ p r o f i l e . s a v e ( ) 
 
         
 
         m e s s a g e s . s u c c e s s ( r e q u e s t ,   f " U s e r   { u s e r . e m a i l }   h a s   b e e n   r e j e c t e d . " ) 
 
         
 
         #   R e t u r n   p a r t i a l   H T M L   f o r   H T M X   o r   r e d i r e c t 
 
         i f   r e q u e s t . h e a d e r s . g e t ( ' H X - R e q u e s t ' ) : 
 
                 r e t u r n   r e n d e r ( r e q u e s t ,   ' a d m i n / p a r t i a l s / u s e r _ r o w . h t m l ' ,   { ' u s e r ' :   u s e r } ) 
 
         
 
         r e t u r n   r e d i r e c t ( ' a d m i n _ u s e r s ' ) 
 
 
 
 @ l o g i n _ r e q u i r e d 
 
 @ u s e r _ p a s s e s _ t e s t ( i s _ s u p e r _ a d m i n ) 
 
 d e f   u s e r _ h i e r a r c h y ( r e q u e s t ) : 
 
         " " " 
 
         V i e w   f o r   d i s p l a y i n g   u s e r   h i e r a r c h y 
 
         " " " 
 
         #   G e t   a l l   e m p l o y e r s   w i t h   t h e i r   e m p l o y e e s 
 
         e m p l o y e r s   =   E m p l o y e r P r o f i l e . o b j e c t s . p r e f e t c h _ r e l a t e d ( 
 
                 ' u s e r ' ,   
 
                 ' e m p l o y e e s ' , 
 
                 ' e m p l o y e e s _ _ u s e r ' 
 
         ) . o r d e r _ b y ( ' c o m p a n y _ n a m e ' ) 
 
         
 
         #   G e t   a d m i n s   ( s u p e r   a d m i n s   a n d   b a n k   a d m i n s ) 
 
         a d m i n s   =   C u s t o m U s e r . o b j e c t s . f i l t e r ( 
 
                 Q ( i s _ s u p e r _ a d m i n = T r u e )   |   Q ( i s _ b a n k _ a d m i n = T r u e ) 
 
         ) . o r d e r _ b y ( ' e m a i l ' ) 
 
         
 
         c o n t e x t   =   { 
 
                 ' e m p l o y e r s ' :   e m p l o y e r s , 
 
                 ' a d m i n s ' :   a d m i n s , 
 
         } 
 
         
 
         r e t u r n   r e n d e r ( r e q u e s t ,   ' a d m i n / u s e r _ h i e r a r c h y . h t m l ' ,   c o n t e x t ) 
 
 
 
 @ l o g i n _ r e q u i r e d 
 
 @ u s e r _ p a s s e s _ t e s t ( i s _ s u p e r _ a d m i n ) 
 
 d e f   e m p l o y e r s _ l i s t ( r e q u e s t ) : 
 
         " " " 
 
         V i e w   f o r   d i s p l a y i n g   a n d   m a n a g i n g   e m p l o y e r   a c c o u n t s 
 
         " " " 
 
         #   G e t   f i l t e r   p a r a m e t e r s 
 
         s t a t u s _ f i l t e r   =   r e q u e s t . G E T . g e t ( ' s t a t u s ' ,   ' ' ) 
 
         s e a r c h _ q u e r y   =   r e q u e s t . G E T . g e t ( ' s e a r c h ' ,   ' ' ) 
 
         s o r t _ b y   =   r e q u e s t . G E T . g e t ( ' s o r t ' ,   ' d a t e _ j o i n e d ' ) 
 
         s o r t _ d i r   =   r e q u e s t . G E T . g e t ( ' d i r ' ,   ' d e s c ' ) 
 
         
 
         #   S t a r t   w i t h   a l l   e m p l o y e r   p r o f i l e s 
 
         e m p l o y e r s _ q u e r y s e t   =   E m p l o y e r P r o f i l e . o b j e c t s . a l l ( ) . s e l e c t _ r e l a t e d ( ' u s e r ' ) 
 
         
 
         #   A p p l y   s t a t u s   f i l t e r 
 
         i f   s t a t u s _ f i l t e r : 
 
                 i f   s t a t u s _ f i l t e r   = =   ' a p p r o v e d ' : 
 
                         e m p l o y e r s _ q u e r y s e t   =   e m p l o y e r s _ q u e r y s e t . f i l t e r ( a p p r o v e d = T r u e ) 
 
                 e l i f   s t a t u s _ f i l t e r   = =   ' p e n d i n g ' : 
 
                         e m p l o y e r s _ q u e r y s e t   =   e m p l o y e r s _ q u e r y s e t . f i l t e r ( a p p r o v e d = F a l s e ) 
 
         
 
         #   A p p l y   s e a r c h   f i l t e r 
 
         i f   s e a r c h _ q u e r y : 
 
                 e m p l o y e r s _ q u e r y s e t   =   e m p l o y e r s _ q u e r y s e t . f i l t e r ( 
 
                         Q ( c o m p a n y _ n a m e _ _ i c o n t a i n s = s e a r c h _ q u e r y )   | 
 
                         Q ( i n d u s t r y _ _ i c o n t a i n s = s e a r c h _ q u e r y )   | 
 
                         Q ( u s e r _ _ e m a i l _ _ i c o n t a i n s = s e a r c h _ q u e r y )   | 
 
                         Q ( u s e r _ _ f i r s t _ n a m e _ _ i c o n t a i n s = s e a r c h _ q u e r y )   | 
 
                         Q ( u s e r _ _ l a s t _ n a m e _ _ i c o n t a i n s = s e a r c h _ q u e r y ) 
 
                 ) . d i s t i n c t ( ) 
 
         
 
         #   A p p l y   s o r t i n g 
 
         i f   s o r t _ b y   = =   ' c o m p a n y ' : 
 
                 o r d e r _ f i e l d   =   ' c o m p a n y _ n a m e '   i f   s o r t _ d i r   = =   ' a s c '   e l s e   ' - c o m p a n y _ n a m e ' 
 
         e l i f   s o r t _ b y   = =   ' e m a i l ' : 
 
                 o r d e r _ f i e l d   =   ' u s e r _ _ e m a i l '   i f   s o r t _ d i r   = =   ' a s c '   e l s e   ' - u s e r _ _ e m a i l ' 
 
         e l i f   s o r t _ b y   = =   ' i n d u s t r y ' : 
 
                 o r d e r _ f i e l d   =   ' i n d u s t r y '   i f   s o r t _ d i r   = =   ' a s c '   e l s e   ' - i n d u s t r y ' 
 
         e l i f   s o r t _ b y   = =   ' s t a t u s ' : 
 
                 o r d e r _ f i e l d   =   ' a p p r o v e d '   i f   s o r t _ d i r   = =   ' a s c '   e l s e   ' - a p p r o v e d ' 
 
         e l s e :     #   d e f a u l t   t o   d a t e   j o i n e d 
 
                 o r d e r _ f i e l d   =   ' u s e r _ _ d a t e _ j o i n e d '   i f   s o r t _ d i r   = =   ' a s c '   e l s e   ' - u s e r _ _ d a t e _ j o i n e d ' 
 
         
 
         e m p l o y e r s _ q u e r y s e t   =   e m p l o y e r s _ q u e r y s e t . o r d e r _ b y ( o r d e r _ f i e l d ) 
 
         
 
         #   C o u n t   e m p l o y e e s   f o r   e a c h   e m p l o y e r 
 
         f o r   e m p l o y e r   i n   e m p l o y e r s _ q u e r y s e t : 
 
                 e m p l o y e r . e m p l o y e e _ c o u n t   =   e m p l o y e r . e m p l o y e e s . c o u n t ( ) 
 
         
 
         #   P a g i n a t i o n 
 
         p a g e _ n u m b e r   =   r e q u e s t . G E T . g e t ( ' p a g e ' ,   1 ) 
 
         p a g i n a t o r   =   P a g i n a t o r ( e m p l o y e r s _ q u e r y s e t ,   2 0 )     #   2 0   e m p l o y e r s   p e r   p a g e 
 
         e m p l o y e r s   =   p a g i n a t o r . g e t _ p a g e ( p a g e _ n u m b e r ) 
 
         
 
         c o n t e x t   =   { 
 
                 ' e m p l o y e r s ' :   e m p l o y e r s , 
 
                 ' s t a t u s _ f i l t e r ' :   s t a t u s _ f i l t e r , 
 
                 ' s e a r c h _ q u e r y ' :   s e a r c h _ q u e r y , 
 
                 ' s o r t _ b y ' :   s o r t _ b y , 
 
                 ' s o r t _ d i r ' :   s o r t _ d i r , 
 
                 ' p a g e _ o b j ' :   e m p l o y e r s , 
 
                 ' t o t a l _ e m p l o y e r s ' :   e m p l o y e r s _ q u e r y s e t . c o u n t ( ) , 
 
                 ' p e n d i n g _ a p p r o v a l _ c o u n t ' :   e m p l o y e r s _ q u e r y s e t . f i l t e r ( a p p r o v e d = F a l s e ) . c o u n t ( ) , 
 
         } 
 
         
 
         r e t u r n   r e n d e r ( r e q u e s t ,   ' a d m i n / e m p l o y e r s . h t m l ' ,   c o n t e x t ) 
 
 
 
 @ l o g i n _ r e q u i r e d 
 
 @ u s e r _ p a s s e s _ t e s t ( i s _ s u p e r _ a d m i n ) 
 
 d e f   c r e a t e _ u s e r ( r e q u e s t ) : 
 
         " " " 
 
         C r e a t e   a   n e w   u s e r 
 
         " " " 
 
         i f   r e q u e s t . m e t h o d   = =   ' P O S T ' : 
 
                 #   E x t r a c t   f o r m   d a t a 
 
                 e m a i l   =   r e q u e s t . P O S T . g e t ( ' e m a i l ' ) 
 
                 f i r s t _ n a m e   =   r e q u e s t . P O S T . g e t ( ' f i r s t _ n a m e ' ) 
 
                 l a s t _ n a m e   =   r e q u e s t . P O S T . g e t ( ' l a s t _ n a m e ' ) 
 
                 r o l e   =   r e q u e s t . P O S T . g e t ( ' r o l e ' ) 
 
                 p a s s w o r d   =   r e q u e s t . P O S T . g e t ( ' p a s s w o r d ' ) 
 
                 
 
                 #   B a s i c   v a l i d a t i o n 
 
                 i f   n o t   a l l ( [ e m a i l ,   r o l e ,   p a s s w o r d ] ) : 
 
                         m e s s a g e s . e r r o r ( r e q u e s t ,   " P l e a s e   f i l l   a l l   r e q u i r e d   f i e l d s . " ) 
 
                         r e t u r n   r e d i r e c t ( ' a d m i n _ c r e a t e _ u s e r ' ) 
 
                 
 
                 #   C h e c k   i f   u s e r   a l r e a d y   e x i s t s 
 
                 i f   C u s t o m U s e r . o b j e c t s . f i l t e r ( e m a i l = e m a i l ) . e x i s t s ( ) : 
 
                         m e s s a g e s . e r r o r ( r e q u e s t ,   f " U s e r   w i t h   e m a i l   { e m a i l }   a l r e a d y   e x i s t s . " ) 
 
                         r e t u r n   r e d i r e c t ( ' a d m i n _ c r e a t e _ u s e r ' ) 
 
                 
 
                 #   C r e a t e   t h e   u s e r 
 
                 u s e r   =   C u s t o m U s e r . o b j e c t s . c r e a t e _ u s e r ( 
 
                         u s e r n a m e = e m a i l , 
 
                         e m a i l = e m a i l , 
 
                         p a s s w o r d = p a s s w o r d , 
 
                         f i r s t _ n a m e = f i r s t _ n a m e , 
 
                         l a s t _ n a m e = l a s t _ n a m e , 
 
                         a p p r o v e d = T r u e     #   A u t o - a p p r o v e   u s e r s   c r e a t e d   b y   a d m i n 
 
                 ) 
 
                 
 
                 #   S e t   r o l e   f l a g s 
 
                 i f   r o l e   = =   ' s u p e r _ a d m i n ' : 
 
                         u s e r . i s _ s u p e r _ a d m i n   =   T r u e 
 
                         u s e r . i s _ s t a f f   =   T r u e 
 
                         u s e r . i s _ s u p e r u s e r   =   T r u e 
 
                 e l i f   r o l e   = =   ' b a n k _ a d m i n ' : 
 
                         u s e r . i s _ b a n k _ a d m i n   =   T r u e 
 
                         u s e r . i s _ s t a f f   =   T r u e 
 
                 e l i f   r o l e   = =   ' e m p l o y e r ' : 
 
                         u s e r . i s _ e m p l o y e r   =   T r u e 
 
                         #   C r e a t e   e m p l o y e r   p r o f i l e 
 
                         c o m p a n y _ n a m e   =   r e q u e s t . P O S T . g e t ( ' c o m p a n y _ n a m e ' ,   ' ' ) 
 
                         r e g i s t r a t i o n _ n u m b e r   =   r e q u e s t . P O S T . g e t ( ' r e g i s t r a t i o n _ n u m b e r ' ,   ' ' ) 
 
                         i n d u s t r y   =   r e q u e s t . P O S T . g e t ( ' i n d u s t r y ' ,   ' ' ) 
 
                         
 
                         i f   n o t   a l l ( [ c o m p a n y _ n a m e ,   r e g i s t r a t i o n _ n u m b e r ] ) : 
 
                                 m e s s a g e s . w a r n i n g ( r e q u e s t ,   f " U s e r   c r e a t e d   b u t   e m p l o y e r   p r o f i l e   i s   i n c o m p l e t e . " ) 
 
                         e l s e : 
 
                                 E m p l o y e r P r o f i l e . o b j e c t s . c r e a t e ( 
 
                                         u s e r = u s e r , 
 
                                         c o m p a n y _ n a m e = c o m p a n y _ n a m e , 
 
                                         r e g i s t r a t i o n _ n u m b e r = r e g i s t r a t i o n _ n u m b e r , 
 
                                         i n d u s t r y = i n d u s t r y , 
 
                                         a p p r o v e d = T r u e 
 
                                 ) 
 
                 e l i f   r o l e   = =   ' e m p l o y e e ' : 
 
                         u s e r . i s _ e m p l o y e e   =   T r u e 
 
                         #   W o u l d   n e e d   e m p l o y e r   I D   t o   c r e a t e   e m p l o y e e   p r o f i l e 
 
                         e m p l o y e r _ i d   =   r e q u e s t . P O S T . g e t ( ' e m p l o y e r _ i d ' ) 
 
                         i f   e m p l o y e r _ i d : 
 
                                 t r y : 
 
                                         e m p l o y e r   =   E m p l o y e r P r o f i l e . o b j e c t s . g e t ( i d = e m p l o y e r _ i d ) 
 
                                         E m p l o y e e P r o f i l e . o b j e c t s . c r e a t e ( 
 
                                                 u s e r = u s e r , 
 
                                                 e m p l o y e r = e m p l o y e r , 
 
                                                 a p p r o v e d = T r u e 
 
                                         ) 
 
                                 e x c e p t   E m p l o y e r P r o f i l e . D o e s N o t E x i s t : 
 
                                         m e s s a g e s . w a r n i n g ( r e q u e s t ,   f " U s e r   c r e a t e d   b u t   e m p l o y e e   p r o f i l e   c o u l d   n o t   b e   l i n k e d   t o   e m p l o y e r . " ) 
 
                 
 
                 u s e r . s a v e ( ) 
 
                 m e s s a g e s . s u c c e s s ( r e q u e s t ,   f " U s e r   { e m a i l }   h a s   b e e n   c r e a t e d   s u c c e s s f u l l y . " ) 
 
                 r e t u r n   r e d i r e c t ( ' a d m i n _ u s e r s ' ) 
 
         
 
         #   G E T   r e q u e s t   -   s h o w   t h e   c r e a t e   u s e r   f o r m 
 
         e m p l o y e r s   =   E m p l o y e r P r o f i l e . o b j e c t s . f i l t e r ( a p p r o v e d = T r u e ) . o r d e r _ b y ( ' c o m p a n y _ n a m e ' ) 
 
         
 
         c o n t e x t   =   { 
 
                 ' e m p l o y e r s ' :   e m p l o y e r s , 
 
         } 
 
         
 
         r e t u r n   r e n d e r ( r e q u e s t ,   ' a d m i n / c r e a t e _ u s e r . h t m l ' ,   c o n t e x t ) 
 
 
 
 @ l o g i n _ r e q u i r e d 
 
 @ u s e r _ p a s s e s _ t e s t ( i s _ s u p e r _ a d m i n ) 
 
 d e f   r e p o r t s ( r e q u e s t ) : 
 
         " " " 
 
         A d m i n   r e p o r t s   v i e w 
 
         " " " 
 
         r e p o r t _ t y p e   =   r e q u e s t . G E T . g e t ( ' t y p e ' ,   ' s u m m a r y ' ) 
 
         d a t e _ r a n g e   =   r e q u e s t . G E T . g e t ( ' d a t e _ r a n g e ' ,   ' a l l ' ) 
 
         
 
         #   B a s e   c o n t e x t 
 
         c o n t e x t   =   { 
 
                 ' r e p o r t _ t y p e ' :   r e p o r t _ t y p e , 
 
                 ' d a t e _ r a n g e ' :   d a t e _ r a n g e , 
 
         } 
 
         
 
         #   A d d i t i o n a l   d a t a   f o r   s u m m a r y   r e p o r t 
 
         i f   r e p o r t _ t y p e   = =   ' s u m m a r y ' : 
 
                 #   U s e r   s t a t i s t i c s 
 
                 t o t a l _ u s e r s   =   C u s t o m U s e r . o b j e c t s . c o u n t ( ) 
 
                 t o t a l _ e m p l o y e e s   =   E m p l o y e e P r o f i l e . o b j e c t s . c o u n t ( ) 
 
                 t o t a l _ e m p l o y e r s   =   E m p l o y e r P r o f i l e . o b j e c t s . c o u n t ( ) 
 
                 
 
                 #   T r i p   s t a t i s t i c s 
 
                 t o t a l _ t r i p s   =   T r i p . o b j e c t s . c o u n t ( ) 
 
                 t o t a l _ c a r b o n _ s a v e d   =   T r i p . o b j e c t s . a g g r e g a t e ( S u m ( ' c a r b o n _ s a v i n g s ' ) ) [ ' c a r b o n _ s a v i n g s _ _ s u m ' ]   o r   0 
 
                 
 
                 #   C a l c u l a t e   a v e r a g e   t r i p s   p e r   e m p l o y e e 
 
                 a v g _ t r i p s _ p e r _ u s e r   =   0 
 
                 i f   t o t a l _ e m p l o y e e s   >   0 : 
 
                         a v g _ t r i p s _ p e r _ u s e r   =   t o t a l _ t r i p s   /   t o t a l _ e m p l o y e e s 
 
                         
 
                 #   C r e d i t   s t a t i s t i c s 
 
                 t o t a l _ c r e d i t s   =   C a r b o n C r e d i t . o b j e c t s . a g g r e g a t e ( S u m ( ' a m o u n t ' ) ) [ ' a m o u n t _ _ s u m ' ]   o r   0 
 
                 r e d e e m e d _ c r e d i t s   =   C a r b o n C r e d i t . o b j e c t s . f i l t e r ( s t a t u s = ' r e d e e m e d ' ) . a g g r e g a t e ( S u m ( ' a m o u n t ' ) ) [ ' a m o u n t _ _ s u m ' ]   o r   0 
 
                 
 
                 #   A d d   s t a t s   t o   c o n t e x t 
 
                 c o n t e x t . u p d a t e ( { 
 
                         ' t o t a l _ u s e r s ' :   t o t a l _ u s e r s , 
 
                         ' t o t a l _ e m p l o y e e s ' :   t o t a l _ e m p l o y e e s , 
 
                         ' t o t a l _ e m p l o y e r s ' :   t o t a l _ e m p l o y e r s , 
 
                         ' t o t a l _ t r i p s ' :   t o t a l _ t r i p s , 
 
                         ' t o t a l _ c a r b o n _ s a v e d ' :   t o t a l _ c a r b o n _ s a v e d , 
 
                         ' a v g _ t r i p s _ p e r _ u s e r ' :   r o u n d ( a v g _ t r i p s _ p e r _ u s e r ,   2 ) , 
 
                         ' t o t a l _ c r e d i t s ' :   t o t a l _ c r e d i t s , 
 
                         ' r e d e e m e d _ c r e d i t s ' :   r e d e e m e d _ c r e d i t s , 
 
                 } ) 
 
         
 
         r e t u r n   r e n d e r ( r e q u e s t ,   ' a d m i n / r e p o r t s . h t m l ' ,   c o n t e x t ) 
 
 
 
 @ l o g i n _ r e q u i r e d 
 
 @ u s e r _ p a s s e s _ t e s t ( i s _ s u p e r _ a d m i n ) 
 
 d e f   e x p o r t _ r e p o r t s ( r e q u e s t ) : 
 
         " " " 
 
         E x p o r t   r e p o r t s   d a t a   i n   C S V   o r   P D F   f o r m a t 
 
         " " " 
 
         r e p o r t _ t y p e   =   r e q u e s t . G E T . g e t ( ' r e p o r t _ t y p e ' ,   ' s u m m a r y ' ) 
 
         d a t e _ r a n g e   =   r e q u e s t . G E T . g e t ( ' d a t e _ r a n g e ' ,   ' a l l ' ) 
 
         f o r m a t   =   r e q u e s t . G E T . g e t ( ' f o r m a t ' ,   ' c s v ' ) 
 
         
 
         #   G e t   d a t a   b a s e d   o n   r e p o r t   t y p e 
 
         d a t a   =   [ ] 
 
         
 
         i f   r e p o r t _ t y p e   = =   ' s u m m a r y ' : 
 
                 #   U s e r   s t a t i s t i c s 
 
                 t o t a l _ u s e r s   =   C u s t o m U s e r . o b j e c t s . c o u n t ( ) 
 
                 t o t a l _ e m p l o y e e s   =   E m p l o y e e P r o f i l e . o b j e c t s . c o u n t ( ) 
 
                 t o t a l _ e m p l o y e r s   =   E m p l o y e r P r o f i l e . o b j e c t s . c o u n t ( ) 
 
                 
 
                 #   T r i p   s t a t i s t i c s 
 
                 t o t a l _ t r i p s   =   T r i p . o b j e c t s . c o u n t ( ) 
 
                 t o t a l _ c a r b o n _ s a v e d   =   T r i p . o b j e c t s . a g g r e g a t e ( S u m ( ' c a r b o n _ s a v i n g s ' ) ) [ ' c a r b o n _ s a v i n g s _ _ s u m ' ]   o r   0 
 
                 
 
                 #   C a l c u l a t e   a v e r a g e   t r i p s   p e r   e m p l o y e e 
 
                 a v g _ t r i p s _ p e r _ u s e r   =   0 
 
                 i f   t o t a l _ e m p l o y e e s   >   0 : 
 
                         a v g _ t r i p s _ p e r _ u s e r   =   t o t a l _ t r i p s   /   t o t a l _ e m p l o y e e s 
 
                         
 
                 #   C r e d i t   s t a t i s t i c s 
 
                 t o t a l _ c r e d i t s   =   C a r b o n C r e d i t . o b j e c t s . a g g r e g a t e ( S u m ( ' a m o u n t ' ) ) [ ' a m o u n t _ _ s u m ' ]   o r   0 
 
                 r e d e e m e d _ c r e d i t s   =   C a r b o n C r e d i t . o b j e c t s . f i l t e r ( s t a t u s = ' r e d e e m e d ' ) . a g g r e g a t e ( S u m ( ' a m o u n t ' ) ) [ ' a m o u n t _ _ s u m ' ]   o r   0 
 
                 
 
                 #   S u m m a r y   d a t a 
 
                 d a t a   =   [ 
 
                         [ ' M e t r i c ' ,   ' V a l u e ' ] , 
 
                         [ ' T o t a l   U s e r s ' ,   t o t a l _ u s e r s ] , 
 
                         [ ' T o t a l   E m p l o y e e s ' ,   t o t a l _ e m p l o y e e s ] , 
 
                         [ ' T o t a l   E m p l o y e r s ' ,   t o t a l _ e m p l o y e r s ] , 
 
                         [ ' T o t a l   T r i p s ' ,   t o t a l _ t r i p s ] , 
 
                         [ ' T o t a l   C a r b o n   S a v e d   ( k g ) ' ,   t o t a l _ c a r b o n _ s a v e d ] , 
 
                         [ ' A v e r a g e   T r i p s   p e r   U s e r ' ,   r o u n d ( a v g _ t r i p s _ p e r _ u s e r ,   2 ) ] , 
 
                         [ ' T o t a l   C r e d i t s ' ,   t o t a l _ c r e d i t s ] , 
 
                         [ ' R e d e e m e d   C r e d i t s ' ,   r e d e e m e d _ c r e d i t s ] 
 
                 ] 
 
         
 
         e l i f   r e p o r t _ t y p e   = =   ' t r i p s ' : 
 
                 #   G e t   t r i p s   b a s e d   o n   d a t e   r a n g e 
 
                 t r i p s   =   T r i p . o b j e c t s . a l l ( ) . s e l e c t _ r e l a t e d ( ' e m p l o y e e ' ,   ' e m p l o y e e _ _ u s e r ' ) . o r d e r _ b y ( ' - s t a r t _ t i m e ' ) 
 
                 
 
                 #   A p p l y   d a t e   f i l t e r   i f   n e e d e d 
 
                 i f   d a t e _ r a n g e   = =   ' 7 d ' : 
 
                         t r i p s   =   t r i p s . f i l t e r ( s t a r t _ t i m e _ _ g t e = t i m e z o n e . n o w ( )   -   t i m e z o n e . t i m e d e l t a ( d a y s = 7 ) ) 
 
                 e l i f   d a t e _ r a n g e   = =   ' 3 0 d ' : 
 
                         t r i p s   =   t r i p s . f i l t e r ( s t a r t _ t i m e _ _ g t e = t i m e z o n e . n o w ( )   -   t i m e z o n e . t i m e d e l t a ( d a y s = 3 0 ) ) 
 
                 e l i f   d a t e _ r a n g e   = =   ' 9 0 d ' : 
 
                         t r i p s   =   t r i p s . f i l t e r ( s t a r t _ t i m e _ _ g t e = t i m e z o n e . n o w ( )   -   t i m e z o n e . t i m e d e l t a ( d a y s = 9 0 ) ) 
 
                 
 
                 #   H e a d e r s 
 
                 d a t a . a p p e n d ( [ ' T r i p   I D ' ,   ' E m p l o y e e ' ,   ' E m p l o y e r ' ,   ' S t a r t   T i m e ' ,   ' E n d   T i m e ' ,   ' T r a n s p o r t   M o d e ' ,   ' D i s t a n c e   ( k m ) ' ,   ' C a r b o n   S a v i n g s   ( k g ) ' ,   ' C r e d i t s   E a r n e d ' ,   ' S t a t u s ' ] ) 
 
                 
 
                 #   T r i p   d a t a 
 
                 f o r   t r i p   i n   t r i p s : 
 
                         d a t a . a p p e n d ( [ 
 
                                 t r i p . i d , 
 
                                 t r i p . e m p l o y e e . u s e r . g e t _ f u l l _ n a m e ( ) , 
 
                                 t r i p . e m p l o y e e . e m p l o y e r . c o m p a n y _ n a m e , 
 
                                 t r i p . s t a r t _ t i m e . s t r f t i m e ( ' % Y - % m - % d   % H : % M ' ) , 
 
                                 t r i p . e n d _ t i m e . s t r f t i m e ( ' % Y - % m - % d   % H : % M ' )   i f   t r i p . e n d _ t i m e   e l s e   ' N / A ' , 
 
                                 t r i p . g e t _ t r a n s p o r t _ m o d e _ d i s p l a y ( ) , 
 
                                 t r i p . d i s t a n c e , 
 
                                 t r i p . c a r b o n _ s a v i n g s , 
 
                                 t r i p . c a r b o n _ c r e d i t s , 
 
                                 ' V e r i f i e d '   i f   t r i p . i s _ v e r i f i e d   e l s e   ' P e n d i n g ' 
 
                         ] ) 
 
         
 
         e l i f   r e p o r t _ t y p e   = =   ' c r e d i t s ' : 
 
                 #   G e t   c r e d i t s   b a s e d   o n   d a t e   r a n g e 
 
                 c r e d i t s   =   C a r b o n C r e d i t . o b j e c t s . a l l ( ) . o r d e r _ b y ( ' - t i m e s t a m p ' ) 
 
                 
 
                 #   A p p l y   d a t e   f i l t e r   i f   n e e d e d 
 
                 i f   d a t e _ r a n g e   = =   ' 7 d ' : 
 
                         c r e d i t s   =   c r e d i t s . f i l t e r ( t i m e s t a m p _ _ g t e = t i m e z o n e . n o w ( )   -   t i m e z o n e . t i m e d e l t a ( d a y s = 7 ) ) 
 
                 e l i f   d a t e _ r a n g e   = =   ' 3 0 d ' : 
 
                         c r e d i t s   =   c r e d i t s . f i l t e r ( t i m e s t a m p _ _ g t e = t i m e z o n e . n o w ( )   -   t i m e z o n e . t i m e d e l t a ( d a y s = 3 0 ) ) 
 
                 e l i f   d a t e _ r a n g e   = =   ' 9 0 d ' : 
 
                         c r e d i t s   =   c r e d i t s . f i l t e r ( t i m e s t a m p _ _ g t e = t i m e z o n e . n o w ( )   -   t i m e z o n e . t i m e d e l t a ( d a y s = 9 0 ) ) 
 
                 
 
                 #   H e a d e r s 
 
                 d a t a . a p p e n d ( [ ' C r e d i t   I D ' ,   ' A m o u n t ' ,   ' S o u r c e   T y p e ' ,   ' O w n e r   T y p e ' ,   ' O w n e r   I D ' ,   ' S t a t u s ' ,   ' T i m e s t a m p ' ,   ' E x p i r y   D a t e ' ] ) 
 
                 
 
                 #   C r e d i t   d a t a 
 
                 f o r   c r e d i t   i n   c r e d i t s : 
 
                         d a t a . a p p e n d ( [ 
 
                                 c r e d i t . i d , 
 
                                 c r e d i t . a m o u n t , 
 
                                 ' T r i p '   i f   c r e d i t . s o u r c e _ t r i p   e l s e   ' S y s t e m ' , 
 
                                 c r e d i t . o w n e r _ t y p e , 
 
                                 c r e d i t . o w n e r _ i d , 
 
                                 c r e d i t . s t a t u s , 
 
                                 c r e d i t . t i m e s t a m p . s t r f t i m e ( ' % Y - % m - % d   % H : % M ' ) , 
 
                                 c r e d i t . e x p i r y _ d a t e . s t r f t i m e ( ' % Y - % m - % d ' )   i f   c r e d i t . e x p i r y _ d a t e   e l s e   ' N / A ' 
 
                         ] ) 
 
         
 
         e l i f   r e p o r t _ t y p e   = =   ' e m p l o y e r s ' : 
 
                 #   G e t   a l l   e m p l o y e r s 
 
                 e m p l o y e r s   =   E m p l o y e r P r o f i l e . o b j e c t s . a l l ( ) . o r d e r _ b y ( ' c o m p a n y _ n a m e ' ) 
 
                 
 
                 #   H e a d e r s 
 
                 d a t a . a p p e n d ( [ ' C o m p a n y   N a m e ' ,   ' I n d u s t r y ' ,   ' T o t a l   E m p l o y e e s ' ,   ' T o t a l   T r i p s ' ,   ' T o t a l   C a r b o n   S a v e d   ( k g ) ' ,   ' T o t a l   C r e d i t s ' ] ) 
 
                 
 
                 #   E m p l o y e r   d a t a 
 
                 f o r   e m p l o y e r   i n   e m p l o y e r s : 
 
                         e m p l o y e e _ c o u n t   =   e m p l o y e r . e m p l o y e e s . c o u n t ( ) 
 
                         
 
                         #   G e t   t r i p s   f o r   t h i s   e m p l o y e r ' s   e m p l o y e e s 
 
                         e m p l o y e e _ i d s   =   e m p l o y e r . e m p l o y e e s . v a l u e s _ l i s t ( ' i d ' ,   f l a t = T r u e ) 
 
                         t r i p s   =   T r i p . o b j e c t s . f i l t e r ( e m p l o y e e _ _ i d _ _ i n = e m p l o y e e _ i d s ) 
 
                         t r i p _ c o u n t   =   t r i p s . c o u n t ( ) 
 
                         c a r b o n _ s a v e d   =   t r i p s . a g g r e g a t e ( S u m ( ' c a r b o n _ s a v i n g s ' ) ) [ ' c a r b o n _ s a v i n g s _ _ s u m ' ]   o r   0 
 
                         
 
                         #   G e t   c r e d i t s   f o r   t h i s   e m p l o y e r 
 
                         c r e d i t s   =   C a r b o n C r e d i t . o b j e c t s . f i l t e r ( o w n e r _ t y p e = ' e m p l o y e r ' ,   o w n e r _ i d = e m p l o y e r . i d ) 
 
                         t o t a l _ c r e d i t s   =   c r e d i t s . a g g r e g a t e ( S u m ( ' a m o u n t ' ) ) [ ' a m o u n t _ _ s u m ' ]   o r   0 
 
                         
 
                         d a t a . a p p e n d ( [ 
 
                                 e m p l o y e r . c o m p a n y _ n a m e , 
 
                                 e m p l o y e r . i n d u s t r y , 
 
                                 e m p l o y e e _ c o u n t , 
 
                                 t r i p _ c o u n t , 
 
                                 c a r b o n _ s a v e d , 
 
                                 t o t a l _ c r e d i t s 
 
                         ] ) 
 
         
 
         #   G e n e r a t e   e x p o r t   b a s e d   o n   f o r m a t 
 
         i f   f o r m a t   = =   ' c s v ' : 
 
                 #   C r e a t e   C S V   r e s p o n s e 
 
                 r e s p o n s e   =   H t t p R e s p o n s e ( c o n t e n t _ t y p e = ' t e x t / c s v ' ) 
 
                 r e s p o n s e [ ' C o n t e n t - D i s p o s i t i o n ' ]   =   f ' a t t a c h m e n t ;   f i l e n a m e = " c a r b o n _ c r e d i t s _ { r e p o r t _ t y p e } _ r e p o r t . c s v " ' 
 
                 
 
                 #   W r i t e   C S V   d a t a 
 
                 w r i t e r   =   c s v . w r i t e r ( r e s p o n s e ) 
 
                 f o r   r o w   i n   d a t a : 
 
                         w r i t e r . w r i t e r o w ( r o w ) 
 
                 
 
                 r e t u r n   r e s p o n s e 
 
         
 
         e l i f   f o r m a t   = =   ' p d f ' : 
 
                 #   F o r   P D F ,   a   m o r e   c o m p l e x   i m p l e m e n t a t i o n   w o u l d   b e   n e e d e d   w i t h   a   P D F   l i b r a r y 
 
                 #   T h i s   i s   a   s i m p l i f i e d   v e r s i o n   t h a t   r e t u r n s   a   t e x t   r e s p o n s e 
 
                 r e s p o n s e   =   H t t p R e s p o n s e ( c o n t e n t _ t y p e = ' t e x t / p l a i n ' ) 
 
                 r e s p o n s e [ ' C o n t e n t - D i s p o s i t i o n ' ]   =   f ' a t t a c h m e n t ;   f i l e n a m e = " c a r b o n _ c r e d i t s _ { r e p o r t _ t y p e } _ r e p o r t . t x t " ' 
 
                 
 
                 #   W r i t e   d a t a   a s   t e x t 
 
                 o u t p u t   =   i o . S t r i n g I O ( ) 
 
                 f o r   r o w   i n   d a t a : 
 
                         o u t p u t . w r i t e ( ' \ t ' . j o i n ( [ s t r ( i t e m )   f o r   i t e m   i n   r o w ] )   +   ' \ n ' ) 
 
                 
 
                 r e s p o n s e . w r i t e ( o u t p u t . g e t v a l u e ( ) ) 
 
                 r e t u r n   r e s p o n s e 
 
         
 
         #   D e f a u l t   f a l l b a c k   -   r e t u r n   J S O N 
 
         r e t u r n   J s o n R e s p o n s e ( { ' d a t a ' :   d a t a } ) 
 
 
 
 #   P r o f i l e   v i e w s 
 
 @ l o g i n _ r e q u i r e d 
 
 @ u s e r _ p a s s e s _ t e s t ( i s _ s u p e r _ a d m i n ) 
 
 d e f   a d m i n _ p r o f i l e ( r e q u e s t ) : 
 
         " " " V i e w   f o r   a d m i n   p r o f i l e   p a g e . " " " 
 
         c o n t e x t   =   { 
 
                 ' p a g e _ t i t l e ' :   ' A d m i n   P r o f i l e ' , 
 
                 ' u s e r ' :   r e q u e s t . u s e r , 
 
         } 
 
         r e t u r n   r e n d e r ( r e q u e s t ,   ' a d m i n / p r o f i l e . h t m l ' ,   c o n t e x t ) 
 
 
 
 @ l o g i n _ r e q u i r e d 
 
 @ u s e r _ p a s s e s _ t e s t ( i s _ s u p e r _ a d m i n ) 
 
 d e f   a d m i n _ u p d a t e _ p r o f i l e ( r e q u e s t ) : 
 
         " " " H a n d l e   a d m i n   p r o f i l e   u p d a t e s . " " " 
 
         i f   r e q u e s t . m e t h o d   = =   ' P O S T ' : 
 
                 #   G e t   f o r m   d a t a 
 
                 f i r s t _ n a m e   =   r e q u e s t . P O S T . g e t ( ' f i r s t _ n a m e ' ) 
 
                 l a s t _ n a m e   =   r e q u e s t . P O S T . g e t ( ' l a s t _ n a m e ' ) 
 
                 e m a i l   =   r e q u e s t . P O S T . g e t ( ' e m a i l ' ) 
 
                 
 
                 #   V a l i d a t e   e m a i l   f o r m a t 
 
                 i f   n o t   e m a i l   o r   ' @ '   n o t   i n   e m a i l : 
 
                         m e s s a g e s . e r r o r ( r e q u e s t ,   " P l e a s e   p r o v i d e   a   v a l i d   e m a i l   a d d r e s s . " ) 
 
                         r e t u r n   r e d i r e c t ( ' a d m i n _ p r o f i l e ' ) 
 
                 
 
                 #   C h e c k   i f   e m a i l   i s   a l r e a d y   i n   u s e   b y   a n o t h e r   u s e r 
 
                 i f   C u s t o m U s e r . o b j e c t s . e x c l u d e ( i d = r e q u e s t . u s e r . i d ) . f i l t e r ( e m a i l = e m a i l ) . e x i s t s ( ) : 
 
                         m e s s a g e s . e r r o r ( r e q u e s t ,   " T h i s   e m a i l   i s   a l r e a d y   i n   u s e   b y   a n o t h e r   u s e r . " ) 
 
                         r e t u r n   r e d i r e c t ( ' a d m i n _ p r o f i l e ' ) 
 
                 
 
                 #   U p d a t e   u s e r   d a t a 
 
                 u s e r   =   r e q u e s t . u s e r 
 
                 u s e r . f i r s t _ n a m e   =   f i r s t _ n a m e 
 
                 u s e r . l a s t _ n a m e   =   l a s t _ n a m e 
 
                 u s e r . e m a i l   =   e m a i l 
 
                 u s e r . s a v e ( ) 
 
                 
 
                 m e s s a g e s . s u c c e s s ( r e q u e s t ,   " P r o f i l e   u p d a t e d   s u c c e s s f u l l y . " ) 
 
                 r e t u r n   r e d i r e c t ( ' a d m i n _ p r o f i l e ' ) 
 
         
 
         #   F o r   G E T   r e q u e s t s ,   r e d i r e c t   t o   p r o f i l e   p a g e 
 
         r e t u r n   r e d i r e c t ( ' a d m i n _ p r o f i l e ' ) 
 
 
 
 @ l o g i n _ r e q u i r e d 
 
 @ u s e r _ p a s s e s _ t e s t ( i s _ s u p e r _ a d m i n ) 
 
 d e f   a d m i n _ c h a n g e _ p a s s w o r d ( r e q u e s t ) : 
 
         " " " H a n d l e   a d m i n   p a s s w o r d   c h a n g e s . " " " 
 
         i f   r e q u e s t . m e t h o d   = =   ' P O S T ' : 
 
                 #   G e t   f o r m   d a t a 
 
                 c u r r e n t _ p a s s w o r d   =   r e q u e s t . P O S T . g e t ( ' c u r r e n t _ p a s s w o r d ' ) 
 
                 n e w _ p a s s w o r d   =   r e q u e s t . P O S T . g e t ( ' n e w _ p a s s w o r d ' ) 
 
                 c o n f i r m _ p a s s w o r d   =   r e q u e s t . P O S T . g e t ( ' c o n f i r m _ p a s s w o r d ' ) 
 
                 
 
                 #   V a l i d a t e   p a s s w o r d s 
 
                 i f   n o t   c u r r e n t _ p a s s w o r d   o r   n o t   n e w _ p a s s w o r d   o r   n o t   c o n f i r m _ p a s s w o r d : 
 
                         m e s s a g e s . e r r o r ( r e q u e s t ,   " P l e a s e   f i l l   i n   a l l   p a s s w o r d   f i e l d s . " ) 
 
                         r e t u r n   r e d i r e c t ( ' a d m i n _ p r o f i l e ' ) 
 
                 
 
                 i f   n e w _ p a s s w o r d   ! =   c o n f i r m _ p a s s w o r d : 
 
                         m e s s a g e s . e r r o r ( r e q u e s t ,   " N e w   p a s s w o r d s   d o   n o t   m a t c h . " ) 
 
                         r e t u r n   r e d i r e c t ( ' a d m i n _ p r o f i l e ' ) 
 
                 
 
                 #   C h e c k   c u r r e n t   p a s s w o r d 
 
                 i f   n o t   r e q u e s t . u s e r . c h e c k _ p a s s w o r d ( c u r r e n t _ p a s s w o r d ) : 
 
                         m e s s a g e s . e r r o r ( r e q u e s t ,   " C u r r e n t   p a s s w o r d   i s   i n c o r r e c t . " ) 
 
                         r e t u r n   r e d i r e c t ( ' a d m i n _ p r o f i l e ' ) 
 
                 
 
                 #   C h a n g e   p a s s w o r d 
 
                 r e q u e s t . u s e r . s e t _ p a s s w o r d ( n e w _ p a s s w o r d ) 
 
                 r e q u e s t . u s e r . s a v e ( ) 
 
                 
 
                 #   U p d a t e   s e s s i o n   t o   p r e v e n t   l o g o u t 
 
                 f r o m   d j a n g o . c o n t r i b . a u t h   i m p o r t   u p d a t e _ s e s s i o n _ a u t h _ h a s h 
 
                 u p d a t e _ s e s s i o n _ a u t h _ h a s h ( r e q u e s t ,   r e q u e s t . u s e r ) 
 
                 
 
                 m e s s a g e s . s u c c e s s ( r e q u e s t ,   " P a s s w o r d   c h a n g e d   s u c c e s s f u l l y . " ) 
 
                 r e t u r n   r e d i r e c t ( ' a d m i n _ p r o f i l e ' ) 
 
         
 
         #   F o r   G E T   r e q u e s t s ,   r e d i r e c t   t o   p r o f i l e   p a g e 
 
         r e t u r n   r e d i r e c t ( ' a d m i n _ p r o f i l e ' ) 
 
 
 
 @ l o g i n _ r e q u i r e d 
 
 @ u s e r _ p a s s e s _ t e s t ( l a m b d a   u :   u . i s _ s u p e r _ a d m i n   o r   u . i s _ b a n k _ a d m i n ) 
 
 d e f   e m p l o y e r _ a p p r o v a l ( r e q u e s t ,   e m p l o y e r _ i d ) : 
 
         " " " 
 
         H a n d l e   e m p l o y e r   a c c o u n t   a p p r o v a l   o r   r e j e c t i o n . 
 
         " " " 
 
         t r y : 
 
                 e m p l o y e r   =   E m p l o y e r P r o f i l e . o b j e c t s . g e t ( i d = e m p l o y e r _ i d ,   a p p r o v e d = F a l s e ) 
 
                 a c t i o n   =   r e q u e s t . G E T . g e t ( ' a c t i o n ' ,   ' ' ) 
 
                 
 
                 i f   a c t i o n   = =   ' a p p r o v e ' : 
 
                         e m p l o y e r . a p p r o v e d   =   T r u e 
 
                         e m p l o y e r . s a v e ( ) 
 
                         
 
                         #   A l s o   a p p r o v e   t h e   u s e r 
 
                         u s e r   =   e m p l o y e r . u s e r 
 
                         u s e r . a p p r o v e d   =   T r u e 
 
                         u s e r . s a v e ( ) 
 
                         
 
                         #   A l l o c a t e   i n i t i a l   c a r b o n   c r e d i t s   t o   t h e   e m p l o y e r   ( i f   n o t   a l r e a d y   d o n e ) 
 
                         i f   n o t   e m p l o y e r . i n i t i a l _ c r e d i t s _ a l l o c a t e d : 
 
                                 #   D e t e r m i n e   i n i t i a l   c r e d i t   a m o u n t   b a s e d   o n   c o m p a n y   s i z e   o r   o t h e r   f a c t o r s 
 
                                 #   F o r   n o w ,   w e ' l l   u s e   a   f i x e d   a m o u n t   o f   1 0 0 0   c r e d i t s 
 
                                 i n i t i a l _ c r e d i t s   =   1 0 0 0 
 
                                 
 
                                 #   C r e a t e   c a r b o n   c r e d i t   r e c o r d 
 
                                 C a r b o n C r e d i t . o b j e c t s . c r e a t e ( 
 
                                         a m o u n t = i n i t i a l _ c r e d i t s , 
 
                                         s o u r c e _ t r i p = N o n e ,     #   N o   a s s o c i a t e d   t r i p   f o r   i n i t i a l   c r e d i t s 
 
                                         o w n e r _ t y p e = ' e m p l o y e r ' , 
 
                                         o w n e r _ i d = e m p l o y e r . i d , 
 
                                         t i m e s t a m p = t i m e z o n e . n o w ( ) , 
 
                                         s t a t u s = ' a c t i v e ' , 
 
                                         e x p i r y _ d a t e = t i m e z o n e . n o w ( )   +   t i m e z o n e . t i m e d e l t a ( d a y s = 3 6 5 )     #   1   y e a r   v a l i d i t y 
 
                                 ) 
 
                                 
 
                                 #   M a r k   a s   a l l o c a t e d 
 
                                 e m p l o y e r . i n i t i a l _ c r e d i t s _ a l l o c a t e d   =   T r u e 
 
                                 e m p l o y e r . s a v e ( ) 
 
                                 
 
                                 m e s s a g e s . s u c c e s s ( 
 
                                         r e q u e s t ,   
 
                                         f " E m p l o y e r   { e m p l o y e r . c o m p a n y _ n a m e }   h a s   b e e n   a p p r o v e d   a n d   a l l o c a t e d   { i n i t i a l _ c r e d i t s }   i n i t i a l   c a r b o n   c r e d i t s . " 
 
                                 ) 
 
                         e l s e : 
 
                                 m e s s a g e s . s u c c e s s ( r e q u e s t ,   f " E m p l o y e r   { e m p l o y e r . c o m p a n y _ n a m e }   h a s   b e e n   a p p r o v e d . " ) 
 
                                 
 
                 e l i f   a c t i o n   = =   ' r e j e c t ' : 
 
                         #   I m p l e m e n t   r e j e c t i o n   l o g i c   h e r e 
 
                         #   Y o u   m a y   w a n t   t o   s e n d   a   n o t i f i c a t i o n   t o   t h e   e m p l o y e r 
 
                         #   F o r   n o w ,   w e ' l l   j u s t   d e l e t e   t h e   e m p l o y e r   a c c o u n t 
 
                         u s e r   =   e m p l o y e r . u s e r 
 
                         e m p l o y e r . d e l e t e ( ) 
 
                         u s e r . d e l e t e ( ) 
 
                         
 
                         m e s s a g e s . s u c c e s s ( r e q u e s t ,   " E m p l o y e r   a c c o u n t   h a s   b e e n   r e j e c t e d   a n d   r e m o v e d . " ) 
 
                         
 
         e x c e p t   E m p l o y e r P r o f i l e . D o e s N o t E x i s t : 
 
                 m e s s a g e s . e r r o r ( r e q u e s t ,   " E m p l o y e r   n o t   f o u n d   o r   a l r e a d y   a p p r o v e d . " ) 
 
                 
 
         r e t u r n   r e d i r e c t ( ' a d m i n _ p e n d i n g _ e m p l o y e r s ' )   
 
 
