SELECT ss.senshi_name sailor_senshi, ss.real_name_jpn real_name, c.name cat, s.school
FROM sailorsenshi ss
LEFT JOIN cats c ON c.id = ss.cat_id
LEFT JOIN schools s ON s.id = ss.school_id