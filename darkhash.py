U
    ��\^;�  �                   @   s   d dl Z ee �d�� dS )�    Ns�:  �                   @   s   d dl Z ee �d�� dS )�    Ns{:  �                   @   s   d dl Z ee �d�� dS )�    Ns�9  �                   @   s�  z0d dl Z d dlZd dlZd dlZd dlmZ W n0   edeeee	eeee	eeee	f � Y nX dZ
dZdZdZdZd	Zd
Z	dZdZdZdZdZdZdZdZdZdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zd d!� Zd"d#� Zd$d%� Zd&d'� Z d(d)� Z!d*d+� Z"d,d-� Z#d.d/� Z$d0d1� Z%d2d3� Z&d4d5� Z'd6d7� Z(d8d9� Z)d:d;� Z*d<d=� Z+d>d?� Z,d@dA� Z-dBdC� Z.dDdE� Z/dFdG� Z0dHdI� Z1e2dJk�r�e1�  dS )K�    N)�BeautifulSoupz�%s[%s!%s] %sModule belum terinstall
%s[%s!%s] %spip install requests bs4
%s[%s!%s] %sKetikan perintah diatas untuk menginstall modulenyaz[0;32mz[1;32mz[0;36mz[1;36mz[0;35mz[1;35mz[0;37mz[1;37mz[0;34mz[1;34mz[0;31mz[1;31mz[1;33mz[0;33mz
[1;97;41mz[0mc            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )NZURL�tools-ixid.ga�
keep-alive�	max-age=0�http://tools-ixid.ga�1�!application/x-www-form-urlencoded�xMozilla/5.0 (Linux; Android 9; RMX1911) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36�|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9� http://tools-ixid.ga/enc-dec.php�#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7�
ZHostZ
ConnectionzCache-ControlZOriginzUpgrade-Insecure-RequestszContent-Typez
User-AgentZAcceptZRefererzAccept-Language�'[1;37m[[1;32m+[1;37m] [0;37mTeks : Z	urlencode�ENCODE�ZmbuttZopeZsubmit�Zheaders�data�html.parser�textarea�no-repeat;">(.*?)</textarea>�   r   �   %s[%s✓%s] %sResult > %s��print�input�requestsZSessionZpostr   ZcontentZfind_all�reZfindall�str�W1�G1�W0�	ZhdZteksZbl�d�rZresZhtmlZrowsZhoh� r$   � �e1   s    
r&   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )NZBASE64r   r   r   r   r   r   r	   r
   r   r   r   r   �base64r   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e2"   s    
r(   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )NZ
CONVERT_UUr   r   r   r   r   r   r	   r
   r   r   r   r   Zurr   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e3.   s    
r)   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )NZJSONr   r   r   r   r   r   r	   r
   r   r   r   r   Zjsonr   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e4:   s    
r*   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )NzGZINFLATE - BASE64 r   r   r   r   r   r   r	   r
   r   r   r   r   Z
gzinflatesr   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e5F   s    
r+   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )NzSTR_ROT13 - BASE64 r   r   r   r   r   r   r	   r
   r   r   r   r   Zstr2r   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e6R   s    
r,   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )NzSTR_ROT13 - GZINFLATE - BASE64 r   r   r   r   r   r   r	   r
   r   r   r   r   Z	gzinflater   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e7^   s    
r-   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )NzGZINFLATE - STR_ROT13 - BASE64r   r   r   r   r   r   r	   r
   r   r   r   r   Z
gzinflaterr   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e8j   s    
r.   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )Nz+GZINFLATE - STR_ROT13 - GZINFLATE - BASE64 r   r   r   r   r   r   r	   r
   r   r   r   r   Z
gzinflatexr   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e9v   s    
r/   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )Nz}STR_ROT13 - CONVERT_UU - URL - GZINFLATE - STR_ROT13 - BASE64 - CONVERT_UU - GZINFLATE - URL - STR_ROT13 - GZINFLATE - BASE64r   r   r   r   r   r   r	   r
   r   r   r   r   Z
gzinflatewr   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e10�   s    
r0   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )Nz*STR_ROT13 - GZINFLATE - STR_ROT13 - BASE64r   r   r   r   r   r   r	   r
   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e11�   s    
r1   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )Nz@BASE64 - GZINFLATE - STR_ROT13 - CONVERT_UU - GZINFLATE - BASE64r   r   r   r   r   r   r	   r
   r   r   r   r   Zurlr   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e12�   s    
r2   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )NzHEX ENCODE-DECODE r   r   r   r   r   r   r	   r
   r   r   r   r   Z	hexencoder   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e13�   s    
r3   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )NzMD5 HASHr   r   r   r   r   r   r	   r
   r   r   r   r   Zmd5r   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e14�   s    
r4   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )Nz	SHA1 HASHr   r   r   r   r   r   r	   r
   r   r   r   r   Zsha1r   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e15�   s    
r5   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )Nz
ROT13 HASHr   r   r   r   r   r   r	   r
   r   r   r   r   Z	str_rot13r   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e16�   s    
r6   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )NZSTRLENr   r   r   r   r   r   r	   r
   r   r   r   r   Zstrlenr   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e17�   s    
r7   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )NZUNESCAPEr   r   r   r   r   r   r	   r
   r   r   r   r   Zxxxr   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e18�   s    
r8   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )NzCHAR ATr   r   r   r   r   r   r	   r
   r   r   r   r   Zbbbr   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e19�   s    
r9   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )NzCHR - BIN2HEX - SUBSTRr   r   r   r   r   r   r	   r
   r   r   r   r   Zaaar   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e20�   s    
r:   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )NZCHRr   r   r   r   r   r   r	   r
   r   r   r   r   Zwwwr   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e21  s    
r;   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )NZHTMLSPECIALCHARSr   r   r   r   r   r   r	   r
   r   r   r   r   Zsssr   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e22  s    
r<   c            	      C   s�   t d� dddddddd	d
dd�
} td�}d
}|ddd�}t�� }|j|| |d�}t|jd�}|�d�}t�	dt
|d ��d }t dtttt|f � d S )NZESCAPEr   r   r   r   r   r   r	   r
   r   r   r   r   Zeeer   r   r   r   r   r   r   r   r   r   r!   r$   r$   r%   �e23  s    
r=   c               	   C   s�   z:t d� t�d�} t dttttf � t�d� t�  W nJ tj	j
k
r�   t�  t d� t dttttf � t�d� t�  Y nX d S )Nr%   zhttp://github.comz%s[%s+%s] %sKoneksi bagus :)r   z!%s[%sx%s] %sTidak ada koneksi -_-)r   r   �getr   r   �G0�time�sleep�logoZ
exceptions�ConnectionError�R1�R0�exit)Zrqr$   r$   r%   �koneksi*  s    



rG   c                   C   s   t �d� tdt � d S )N�clearz�%s _____              __     _______               __    
|     \.---.-.----.|  |--.|   |   |.---.-.-----.|  |--.
|  --  |  _  |   _||    < |       ||  _  |__ --||     |
|_____/|___._|__|  |__|__||___|___||___._|_____||__|__|)�os�systemr   r   r$   r$   r$   r%   rB   7  s    
�rB   c                f   C   s�   t dttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttfd � d S )Na�  
%s[%s 01 %s] %sURL
%s[%s 02 %s] %sBASE64
%s[%s 03 %s] %sCONVERT_UU
%s[%s 04 %s] %sJSON
%s[%s 05 %s] %sGZINFLATE - BASE64
%s[%s 06 %s] %sSTR_ROT13 - BASE64
%s[%s 07 %s] %sSTR_ROT13 - GZINFLATE - BASE64
%s[%s 08 %s] %sGZINFLATE - STR_ROT13 - BASE64 
%s[%s 09 %s] %sGZINFLATE - STR_ROT13 - GZINFLATE - BASE64
%s[%s 10 %s] %sSTR_ROT13 - CONVERT_UU - URL - GZINFLATE - 
       STR_ROT13 - BASE64 - CONVERT_UU - GZINFLATE - URL - 
       STR_ROT13 - GZINFLATE - BASE64
%s[%s 11 %s] %sSTR_ROT13 - GZINFLATE - STR_ROT13 - BASE64
%s[%s 12 %s] %sBASE64 - GZINFLATE - STR_ROT13 - CONVERT_UU - 
       GZINFLATE - BASE64
%s[%s 13 %s] %sHEX ENCODE-DECODE 
%s[%s 14 %s] %sMD5 HASH
%s[%s 15 %s] %sSHA1 HASH 
%s[%s 16 %s] %sROT13 HASH
%s[%s 17 %s] %sSTRLEN
%s[%s 18 %s] %sUNESCAPE
%s[%s 19 %s] %sCHAR AT 
%s[%s 20 %s] %sCHR - BIN2HEX - SUBSTR 
%s[%s 21 %s] %sCHR
%s[%s 22 %s] %sHTMLSPECIALCHARS
%s[%s 23 %s] %sESCAPE

%s[%s C/c %s] %sContact (Whatsapp)
%s[%s E/e %s] %sExit
)r   r   �C1r    rD   rE   r$   r$   r$   r%   �menu=  s    ��rL   c                  C   s~  t �  t�  ddddddddd	d
dddddddddddddddddg} tdtttttttttf	 �}|| kr�t �  t�  tdttttf � tdtttttttttf	 �}qd|dkr�t �  t	�  td� t
�  �n�|dkr�t �  t	�  td� t�  �n�|dk�r t �  t	�  td� t�  �nZ|dk�rHt �  t	�  td� t�  �n2|d	k�rpt �  t	�  td� t�  �n
|d
k�r�t �  t	�  td� t�  �n�|dk�r�t �  t	�  td� t�  �n�|dk�r�t �  t	�  td� t�  �n�|dk�rt �  t	�  td� t�  �nj|dk�r8t �  t	�  td� t�  �nB|dk�r`t �  t	�  td� t�  �n|dk�r�t �  t	�  td� t�  �n�|dk�r�t �  t	�  td� t�  �n�|dk�r�t �  t	�  td� t�  �n�|dk�r t �  t	�  td� t�  �nz|dk�r(t �  t	�  td� t�  �nR|dk�rPt �  t	�  td� t�  �n*|dk�rxt �  t	�  td� t�  �n|dk�r�t �  t	�  td� t�  n�|dk�r�t �  t	�  td� t�  n�|dk�r�t �  t	�  td� t�  n�|dk�rt �  t	�  td� t�  nj|dk�r6t �  t	�  td� t �  nD|dk�sJ|dk�rTt!d� n&|dk�sh|dk�rzt"�#d � t!d� d S )!N�E�e�C�cr   �2�3�4�5�6�7�8�9Z10Z11Z12Z13Z14Z15Z16Z17Z18Z19Z20Z21Z22Z23u0   %s╔>%s[%sD4RK5H4D0W5%s]
%s╚%s[%sPilih%s]> %sz
%s[%sx%s] %sPilihan Anda salahr%   r   z>xdg-open https://wa.me/628996604524?text=Assalamualaikum%20gan)$rB   rL   r   r   r   �P1r    r   rE   rG   r&   r(   r)   r*   r+   r,   r-   r.   r/   r0   r1   r2   r3   r4   r5   r6   r7   r8   r9   r:   r;   r<   r=   rF   rI   rJ   )ZsuZpilr$   r$   r%   �inpZ  s   : 








































rZ   �__main__)3r   r   rI   r@   Zbs4r   r   r   rD   r    r?   r   ZC0rK   ZP0rY   ZB0ZB1rE   ZY1ZY0ZBGZREr&   r(   r)   r*   r+   r,   r-   r.   r/   r0   r1   r2   r3   r4   r5   r6   r7   r8   r9   r:   r;   r<   r=   rG   rB   rL   rZ   �__name__r$   r$   r$   r%   �<module>   sd    * 
)�marshal�exec�loads� r   r   � �<module>   s   )�marshal�exec�loads� r   r   � �<module>   s   )�marshal�exec�loads� r   r   �$/storage/emulated/legacy/darkhash.py�<module>   s   