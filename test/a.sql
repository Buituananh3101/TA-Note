
SELECT K.HOTEN
FROM KHACH K
WHERE k.makh in (
    select tmp.makh
    from (
        SELECT H.MAKH, COUNT(CT.MASP) AS SoLuong
        FROM HOADON H
        JOIN CTHD CT ON H.SOHD = CT.SOHD
        GROUP BY H.MAKH
        ) as tmp
    where tmp.SoLuong = (SELECT MAX(SoLuong) FROM SoLuongMatHang)
    )
)